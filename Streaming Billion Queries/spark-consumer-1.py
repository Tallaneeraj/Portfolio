
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

KAFKA_BROKERS = "localhost:29092,localhost:39092,localhost:49092"
TOPIC_NAME = "Transaction"

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("KafkaSparkConsumer") \
    .getOrCreate()

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
    .option("startingOffsets", "earliest") \
    .load()

# Deserialize JSON Messages
transaction_df = kafka_stream.selectExpr("CAST(value AS STRING)")
transaction_df = transaction_df.withColumn("data", from_json(col("value"), schema)).select("data.*")

# Write Stream to Console
query = transaction_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", False) \
    .start()

query.awaitTermination()
