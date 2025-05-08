import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext

args = getResolvedOptions(sys.argv, ['Data_collection'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

datasource = glueContext.create_dynamic_frame.from_catalog(
    database="sensor_database",
    table_name="sensor_data"
)

transformed = ApplyMapping.apply(frame=datasource, mappings=[
    ("sensor_id", "string", "sensor_id", "string"),
    ("temperature", "double", "temperature", "double"),
    ("timestamp", "double", "timestamp", "timestamp")
])

glueContext.write_dynamic_frame.from_options(
    frame=transformed,
    connection_type="s3",
    connection_options={"path": "s3://sensor-data/"},
    format="parquet"
)
