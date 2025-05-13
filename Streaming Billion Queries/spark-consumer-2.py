from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_json, struct, sum, count
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

KAFKA_BROKERS = "localhost:29092,localhost:39092,localhost:49092"
TOPIC_NAME = "Transaction"
OUTPUT_TOPIC = "AggregatedTransactions"
CHECKPOINT_DIR = '/mnt/spark-checkpoints'
STATE_DIR = '/mnt/spark-state'

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1') \
    .config('spark.sql.streaming.checkpointLocation', CHECKPOINT_DIR) \
    .config('spark.sql.streaming.stateStore.stateStoreDir', STATE_DIR) \
    .config('spark.sql.shuffle.partitions', 20) \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define Schema for Transaction Data
schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("userID", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("transactionTime", IntegerType(), True),
    StructField("merchantID", StringType(), True),
    StructField("transactionType", StringType(), True),
    StructField("paymentMethod", StringType(), True),
    StructField("currency", StringType(), True)
])

# Read Stream from Kafka
kafka_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKERS) \
    .option("subscribe", TOPIC_NAME) \
    .option("startingOffsets", "earliest").option("failOnDataLoss", "false") \
    .load()

# Deserialize JSON Messages
transaction_df = kafka_stream.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Convert transactionTime to timestamp
transaction_df = transaction_df.select(
    col("transaction_id"),
    col("userID"),
    col("amount"),
    col("transactionTime"),
    col("merchantID"),
    col("transactionType"),
    col("paymentMethod"),
    col("currency"),
    (col("transactionTime") / 1000).cast("timestamp").alias("transactionTimestamp")
)



# Aggregate transactions per merchant
aggregated_df = transaction_df.withWatermark("transactionTimestamp", "10 minutes").groupBy("merchantID") \
    .agg(sum("amount").alias('totalAmount'), count("*").alias("transactionCount"))

# Convert aggregated data to Kafka output format
aggregation_query = aggregated_df.withColumn("key", col('merchantID').cast("string")) \
    .withColumn("value", to_json(struct(
        col("merchantID"),
        col("totalAmount"),
        col("transactionCount")
    ))) \
    .selectExpr("key", "value") \
    .writeStream \
    .format('kafka') \
    .outputMode('update') \
    .trigger(processingTime='30 seconds')\
    .option("kafka.bootstrap.servers", KAFKA_BROKERS) \
    .option('topic', OUTPUT_TOPIC) \
    .option('checkpointLocation', f'{CHECKPOINT_DIR}/aggregates') \
    .start()

aggregation_query.awaitTermination()

