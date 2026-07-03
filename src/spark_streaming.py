from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, avg, count, window
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType

print("🚀 Starting Spark Streaming Consumer...")

# Create Spark Session
spark = SparkSession.builder \
    .appName("RealTimeFinancialStreaming") \
    .config("spark.jars.packages", 
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("✅ Spark Session created!")

# Define Schema
schema = StructType([
    StructField("symbol", StringType()),
    StructField("price", DoubleType()),
    StructField("volume", LongType()),
    StructField("timestamp", StringType()),
    StructField("change_pct", DoubleType()),
    StructField("market", StringType()),
    StructField("source", StringType())
])

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "financial-transactions") \
    .option("startingOffsets", "latest") \
    .load()

print("✅ Connected to Kafka topic!")

# Parse JSON
parsed_df = df.select(
    from_json(col("value").ca
