from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

# Define the schema for the JSON data
schema = StructType([
    StructField("id", StringType(), True),
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("address", StringType(), True),
    StructField("post_code", StringType(), True),
    StructField("email", StringType(), True),
    StructField("username", StringType(), True),
    StructField("dob", StringType(), True),
    StructField("registered_date", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("picture", StringType(), True)
])

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkCassandra") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .getOrCreate()

# Read data from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "info_topic") \
    .load()

# Parse the JSON data
df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Write data to Cassandra
df.writeStream \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write \
                  .format("org.apache.spark.sql.cassandra") \
                  .mode("append") \
                  .options(table="user_data", keyspace="user_keyspace") \
                  .save()) \
    .outputMode("append") \
    .start() \
    .awaitTermination()
