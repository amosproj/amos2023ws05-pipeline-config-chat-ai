import json

data = [
    {
        "q1": "I would like to use RTDIP components to read from an eventhub using 'connection string' as the connection string, and 'consumer group' as the consumer group, transform using binary to string, and edge x transformer then write to delta",
        "c1": """
from rtdip_sdk.pipelines.sources import SparkEventhubSource
from rtdip_sdk.pipelines.transformers import BinaryToStringTransformer, EdgeXTransformer  # Assuming EdgeXTransformer is correct
from rtdip_sdk.pipelines.destinations import SparkDeltaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility
import json

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# EventHub configuration
ehConf = {
    "eventhubs.connectionString": "your_connection_string_here",
    "eventhubs.consumerGroup": "your_consumer_group_here",
    "eventhubs.startingPosition": json.dumps(
        {"offset": "0", "seqNo": -1, "enqueuedTime": None, "isInclusive": True}
    ),
}

# Read data from EventHub
source = SparkEventhubSource(spark, ehConf).read_batch()

# Transform binary data to string
string_data = BinaryToStringTransformer(source, "body", "body").transform()

# Apply Edge X transformation
edge_transformed_data = EdgeXTransformer(string_data, "body").transform()

# Write the transformed data to Delta
SparkDeltaDestination(
    data=edge_transformed_data, 
    options={
        "spark.sql.warehouse.dir": "your_spark_warehouse_directory_here",
    }, 
    destination="your_delta_table_name_here"
).write_batch()
""",
        "q2": "I need to read data from Kafka using a specific bootstrap server and topic, then apply a JSON parser, and finally write the results to a Hive table.",
        "c2": """
from rtdip_sdk.pipelines.sources import KafkaSource
from rtdip_sdk.pipelines.transformers import JsonParserTransformer
from rtdip_sdk.pipelines.destinations import HiveDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Kafka configuration
kafkaConf = {
    "kafka.bootstrap.servers": "your_bootstrap_server_here",
    "subscribe": "your_topic_here"
}

# Read data from Kafka
source = KafkaSource(spark, kafkaConf).read_stream()

# Transform data using JSON parser
parsed_data = JsonParserTransformer(source, "value").transform()

# Write the transformed data to Hive
HiveDestination(
    data=parsed_data,
    table_name="your_hive_table_name_here"
).write_batch()
""" ,

    "q3": "Fetch sensor data from an Azure Blob Storage in CSV format, aggregate the data on sensor ID, and save it to a SQL database.",
    "c3":"""
from rtdip_sdk.pipelines.sources import AzureBlobStorageSource
from rtdip_sdk.pipelines.transformers import AggregationTransformer
from rtdip_sdk.pipelines.destinations import SQLDatabaseDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Azure Blob Storage configuration
blobConf = {
    "storage_account_name": "your_storage_account_name",
    "container_name": "your_container_name",
    "file_type": "csv"
}

# Read data from Azure Blob Storage
source = AzureBlobStorageSource(spark, blobConf).read_batch()

# Aggregate data on sensor ID
aggregated_data = AggregationTransformer(source, "sensor_id").transform()

# Write the aggregated data to SQL database
SQLDatabaseDestination(
    data=aggregated_data,
    database_url="your_database_url",
    table_name="your_table_name_here"
).write_batch()

""",

    "q4" : "Stream data from a MQTT broker, filter out readings below a threshold value, and store the data in Elasticsearch.",
    "c4": """
from rtdip_sdk.pipelines.sources import MQTTSource
from rtdip_sdk.pipelines.transformers import FilterTransformer
from rtdip_sdk.pipelines.destinations import ElasticsearchDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# MQTT configuration
mqttConf = {
    "broker_url": "your_broker_url",
    "topic": "your_topic_here"
}

# Read data from MQTT
source = MQTTSource(spark, mqttConf).read_stream()

# Filter data based on a threshold
filtered_data = FilterTransformer(source, "reading", ">", "threshold_value").transform()

# Write the filtered data to Elasticsearch
ElasticsearchDestination(
    data=filtered_data,
    elasticsearch_url="your_elasticsearch_url",
    index_name="your_index_name_here"
).write_batch()

""",
    "q5": "Import financial data from an S3 bucket in Parquet format, apply a standard scaler transformation, and then upload it to a Redshift database.",
    "c5":
    """

from rtdip_sdk.pipelines.sources import S3Source
from rtdip_sdk.pipelines.transformers import StandardScalerTransformer
from rtdip_sdk.pipelines.destinations import RedshiftDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# S3 bucket configuration
s3Conf = {
    "bucket_name": "your_bucket_name",
    "file_type": "parquet",
    "file_path": "your_file_path"
}

# Read data from S3
source = S3Source(spark, s3Conf).read_batch()

# Apply standard scaler transformation
scaled_data = StandardScalerTransformer(source, "financial_column").transform()

# Write the scaled data to Redshift
RedshiftDestination(
    data=scaled_data,
    redshift_url="your_redshift_url",
    table_name="your_table_name_here"
).write_batch()
""",

    "q6": "Retrieve temperature data from a REST API, normalize the data, and write it into a MongoDB collection.",
    "c6": """
from rtdip_sdk.pipelines.sources import RestAPISource
from rtdip_sdk.pipelines.transformers import NormalizationTransformer
from rtdip_sdk.pipelines.destinations import MongoDBDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# REST API configuration
apiConf = {
    "url": "http://your_api_endpoint",
    "method": "GET"
}

# Read data from REST API
source = RestAPISource(spark, apiConf).read_batch()

# Normalize temperature data
normalized_data = NormalizationTransformer(source, "temperature").transform()

# Write normalized data to MongoDB
MongoDBDestination(
    data=normalized_data,
    mongodb_url="your_mongodb_url",
    database_name="your_database_name",
    collection_name="your_collection_name"
).write_batch()

""",

    "q7":"Connect to a Google Cloud Storage, download logs in JSON format, conduct sentiment analysis, and then store the results in a Google BigQuery table.",
    "c7": """
from rtdip_sdk.pipelines.sources import GCSSource
from rtdip_sdk.pipelines.transformers import SentimentAnalysisTransformer
from rtdip_sdk.pipelines.destinations import BigQueryDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Google Cloud Storage configuration
gcsConf = {
    "bucket_name": "your_gcs_bucket_name",
    "file_type": "json",
    "file_path": "your_logs_path"
}

# Read data from Google Cloud Storage
source = GCSSource(spark, gcsConf).read_batch()

# Perform sentiment analysis
sentiment_data = SentimentAnalysisTransformer(source, "log_text").transform()

# Write sentiment analysis results to Google BigQuery
BigQueryDestination(
    data=sentiment_data,
    bigquery_url="your_bigquery_url",
    table_name="your_bigquery_table_name"
).write_batch()
""",

    "q8": "Stream Twitter data using API credentials, extract hashtags from tweets, and save the data into a Cassandra database.",
    "c8": """
from rtdip_sdk.pipelines.sources import TwitterAPISource
from rtdip_sdk.pipelines.transformers import HashtagExtractorTransformer
from rtdip_sdk.pipelines.destinations import CassandraDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Twitter API configuration
twitterConf = {
    "api_key": "your_api_key",
    "api_secret_key": "your_api_secret_key",
    "access_token": "your_access_token",
    "access_token_secret": "your_access_token_secret"
}

# Read data from Twitter API
source = TwitterAPISource(spark, twitterConf).read_stream()

# Extract hashtags from tweets
hashtag_data = HashtagExtractorTransformer(source, "tweet_text").transform()

# Write the data to Cassandra
CassandraDestination(
    data=hashtag_data,
    cassandra_url="your_cassandra_url",
    keyspace="your_keyspace",
    table_name="your_table_name"
).write_batch()
""",
    "q9": "Load sales data from an FTP (file transfer protocol) server, perform currency conversion, and append the results to an existing Parquet file.",
    "c9": """
from rtdip_sdk.pipelines.sources import FTPSource
from rtdip_sdk.pipelines.transformers import CurrencyConversionTransformer
from rtdip_sdk.pipelines.destinations import ParquetFileDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# FTP server configuration
ftpConf = {
    "server_url": "ftp://your_ftp_server",
    "username": "your_username",
    "password": "your_password",
    "file_path": "your_sales_data_path"
}

# Read data from FTP server
source = FTPSource(spark, ftpConf).read_batch()

# Perform currency conversion
converted_data = CurrencyConversionTransformer(source, "sales_amount", "USD_to_EUR").transform()

# Append data to an existing Parquet file
ParquetFileDestination(
    data=converted_data,
    file_path="your_parquet_file_path",
    mode="append"
).write_batch()
""",
    "q10":"Connect to an IoT device using MQTT protocol, apply a low-pass filter to sensor readings, and upload the filtered data to an InfluxDB instance.",
    "c10":"""
from rtdip_sdk.pipelines.sources import MQTTSource
from rtdip_sdk.pipelines.transformers import LowPassFilterTransformer
from rtdip_sdk.pipelines.destinations import InfluxDBDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# MQTT configuration
mqttConf = {
    "broker_url": "mqtt://your_mqtt_broker",
    "topic": "your_topic"
}

# Read data from IoT device
source = MQTTSource(spark, mqttConf).read_stream()

# Apply low-pass filter
filtered_data = LowPassFilterTransformer(source, "sensor_reading").transform()

# Write the filtered data to InfluxDB
InfluxDBDestination(
    data=filtered_data,
    influxdb_url="your_influxdb_url",
    database_name="your_database_name"
).write_batch()
""",
    "q11":"Read customer feedback from a Google Sheets document, apply sentiment analysis, and store the results in a PostgreSQL database for further analysis.",
    "c11":"""
from rtdip_sdk.pipelines.sources import GoogleSheetsSource
from rtdip_sdk.pipelines.transformers import SentimentAnalysisTransformer
from rtdip_sdk.pipelines.destinations import PostgreSQLDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Google Sheets configuration
sheetsConf = {
    "document_id": "your_document_id",
    "range": "Sheet1!A1:C100"
}

# Read data from Google Sheets
source = GoogleSheetsSource(spark, sheetsConf).read_batch()

# Apply sentiment analysis
analyzed_data = SentimentAnalysisTransformer(source, "feedback_column").transform()

# Write the analyzed data to PostgreSQL
PostgreSQLDestination(
    data=analyzed_data,
    postgresql_url="your_postgresql_url",
    table_name="customer_feedback_analysis"
).write_batch()
""",

    "q12":"Aggregate temperature and humidity data from a CSV file stored in an Azure Data Lake, calculate average values per day, and upload to a Snowflake database.",
    "c12": """
from rtdip_sdk.pipelines.sources import AzureDataLakeSource
from rtdip_sdk.pipelines.transformers import DailyAverageTransformer
from rtdip_sdk.pipelines.destinations import SnowflakeDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Azure Data Lake configuration
adlConf = {
    "storage_account_name": "your_account_name",
    "file_system_name": "your_file_system",
    "file_path": "your_file_path.csv"
}

# Read data from Azure Data Lake
source = AzureDataLakeSource(spark, adlConf).read_batch()

# Calculate daily averages
daily_averages = DailyAverageTransformer(source, ["temperature", "humidity"]).transform()

# Write the daily averages to Snowflake
SnowflakeDestination(
    data=daily_averages,
    snowflake_url="your_snowflake_url",
    table_name="daily_temperature_humidity"
).write_batch()
""",

    "q13":"Extract stock market data from a REST API, calculate moving averages, and save the data in an Amazon Redshift cluster.",
    "c13":"""
from rtdip_sdk.pipelines.sources import RestAPISource
from rtdip_sdk.pipelines.transformers import MovingAverageTransformer
from rtdip_sdk.pipelines.destinations import RedshiftDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# REST API configuration
apiConf = {
    "url": "http://api.example.com/stock_data",
    "method": "GET"
}

# Read data from REST API
source = RestAPISource(spark, apiConf).read_batch()

# Calculate moving averages
moving_avg_data = MovingAverageTransformer(source, "stock_price").transform()

# Write the moving average data to Amazon Redshift
RedshiftDestination(
    data=moving_avg_data,
    redshift_url="your_redshift_url",
    table_name="stock_moving_averages"
).write_batch()
""",
    "q14": "Access weather data stored in an HDFS cluster, normalize temperature readings, and store the results in an Elasticsearch index.",
    "c14": """
from rtdip_sdk.pipelines.sources import HDFSSource
from rtdip_sdk.pipelines.transformers import NormalizationTransformer
from rtdip_sdk.pipelines.destinations import ElasticsearchDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# HDFS configuration
hdfsConf = {
    "hdfs_url": "hdfs://your_hdfs_cluster",
    "file_path": "/path/to/weather_data.parquet",
    "file_type": "parquet"
}

# Read data from HDFS
source = HDFSSource(spark, hdfsConf).read_batch()

# Normalize temperature readings
normalized_data = NormalizationTransformer(source, "temperature").transform()

# Store the results in an Elasticsearch index
ElasticsearchDestination(
    data=normalized_data,
    elasticsearch_url="http://your_elasticsearch_server",
    index_name="weather_data"
).write_batch()
""",
    "q15":"Load sales records from a MongoDB collection, filter out records with sales below $500, and export the data to a CSV file.",
    "c15":"""
from rtdip_sdk.pipelines.sources import MongoDBSource
from rtdip_sdk.pipelines.transformers import FilterTransformer
from rtdip_sdk.pipelines.destinations import CSVFileDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# MongoDB configuration
mongoConf = {
    "mongodb_url": "mongodb://your_mongodb_server",
    "database_name": "sales_db",
    "collection_name": "sales_records"
}

# Read data from MongoDB
source = MongoDBSource(spark, mongoConf).read_batch()

# Filter records with sales below $500
filtered_data = FilterTransformer(source, "sales_amount", ">", 500).transform()

# Export the data to a CSV file
CSVFileDestination(
    data=filtered_data,
    file_path="/path/to/your_output_file.csv"
).write_batch()
""",
    "q16":"Stream social media data from a JSON file, deduplicate the entries based on user ID, and store the results in a Delta Lake.",
    "c16": """
from rtdip_sdk.pipelines.sources import JSONFileSource
from rtdip_sdk.pipelines.transformers import DeduplicationTransformer
from rtdip_sdk.pipelines.destinations import DeltaLakeDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# JSON file configuration
jsonConf = {
    "file_path": "/path/to/social_media_data.json"
}

# Read data from JSON file
source = JSONFileSource(spark, jsonConf).read_stream()

# Deduplicate entries based on user ID
deduplicated_data = DeduplicationTransformer(source, "user_id").transform()

# Store the results in Delta Lake
DeltaLakeDestination(
    data=deduplicated_data,
    delta_path="/path/to/delta_lake/social_media"
).write_batch()
""",

    "q17": "Load IoT sensor data from a CSV file, apply a smoothing filter to the readings, and write to a Delta Lake for time-series analysis.",
    "c17":"""
from rtdip_sdk.pipelines.sources import CSVFileSource
from rtdip_sdk.pipelines.transformers import SmoothingFilterTransformer
from rtdip_sdk.pipelines.destinations import DeltaLakeDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# CSV file configuration
csvConf = {
    "file_path": "/path/to/iot_sensor_data.csv",
    "options": {"header": True, "inferSchema": True}
}

# Read data from CSV file
source = CSVFileSource(spark, csvConf).read_batch()

# Apply smoothing filter
smoothed_data = SmoothingFilterTransformer(source, "sensor_reading").transform()

# Write the smoothed data to Delta Lake
DeltaLakeDestination(
    data=smoothed_data,
    delta_path="/path/to/delta_lake/iot_sensor"
).write_batch()

""",
    "q18": "Read customer purchase history from a Parquet file, perform a customer segmentation analysis, and save the segments to a Delta Lake.",

    "c18": """

from rtdip_sdk.pipelines.sources import ParquetFileSource
from rtdip_sdk.pipelines.transformers import CustomerSegmentationTransformer
from rtdip_sdk.pipelines.destinations import DeltaLakeDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Parquet file configuration
parquetConf = {
    "file_path": "/path/to/customer_purchase_history.parquet"
}

# Read data from Parquet file
source = ParquetFileSource(spark, parquetConf).read_batch()

# Perform customer segmentation analysis
segmented_data = CustomerSegmentationTransformer(source, "purchase_data").transform()

# Save the segments to Delta Lake
DeltaLakeDestination(
    data=segmented_data,
    delta_path="/path/to/delta_lake/customer_segments"
).write_batch()
""",
    "q19": "Aggregate financial transaction data from a SQL database, calculate the monthly average transaction amount, and store the results in a Delta Lake.",
    "c19": """
from rtdip_sdk.pipelines.sources import SQLDatabaseSource
from rtdip_sdk.pipelines.transformers import MonthlyAverageTransformer
from rtdip_sdk.pipelines.destinations import DeltaLakeDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# SQL database configuration
sqlConf = {
    "database_url": "jdbc:mysql://your_database_url",
    "table_name": "financial_transactions",
    "user": "your_username",
    "password": "your_password"
}

# Read data from SQL database
source = SQLDatabaseSource(spark, sqlConf).read_batch()

# Calculate monthly average transaction amount
monthly_avg_data = MonthlyAverageTransformer(source, "transaction_amount").transform()

# Store the results in Delta Lake
DeltaLakeDestination(
    data=monthly_avg_data,
    delta_path="/path/to/delta_lake/financial_averages"
).write_batch()
""",
    "q20":"Fetch log data from an Elasticsearch index, filter logs with error severity, and archive them in a Delta Lake.",
    "c20": """
from rtdip_sdk.pipelines.sources import ElasticsearchSource
from rtdip_sdk.pipelines.transformers import LogSeverityFilterTransformer
from rtdip_sdk.pipelines.destinations import DeltaLakeDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# Elasticsearch configuration
esConf = {
    "elasticsearch_url": "http://your_elasticsearch_server",
    "index_name": "log_data"
}

# Read data from Elasticsearch
source = ElasticsearchSource(spark, esConf).read_batch()

# Filter logs with error severity
error_logs = LogSeverityFilterTransformer(source, "severity", "ERROR").transform()

# Archive logs in Delta Lake
DeltaLakeDestination(
    data=error_logs,
    delta_path="/path/to/delta_lake/error_logs"
).write_batch()
""",

    "q21": "Read weather data from a RESTful API, convert temperature from Celsius to Fahrenheit, and store the results in a JSON file.",
    "c21":"""
from rtdip_sdk.pipelines.sources import RestAPISource
from rtdip_sdk.pipelines.transformers import CelsiusToFahrenheitTransformer
from rtdip_sdk.pipelines.destinations import JSONFileDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# REST API configuration
restApiConf = {
    "url": "https://api.weatherapi.com/v1/current.json?key=your_api_key&q=London"
}

# Read data from RESTful API
source = RestAPISource(spark, restApiConf).read_batch()

# Convert temperature from Celsius to Fahrenheit
converted_data = CelsiusToFahrenheitTransformer(source, "temp_c").transform()

# Store the results in a JSON file
JSONFileDestination(
    data=converted_data,
    file_path="/path/to/output_weather_data.json"
).write_batch()
""",

    "q22":"Connect to a MySQL database, retrieve order data, group by product category, and insert the grouped data into a new table.",
    "c22":"""
from rtdip_sdk.pipelines.sources import SQLDatabaseSource
from rtdip_sdk.pipelines.transformers import GroupByTransformer
from rtdip_sdk.pipelines.destinations import SQLDatabaseDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# MySQL database source configuration
mysqlSourceConf = {
    "database_url": "jdbc:mysql://your_mysql_server:3306/your_database",
    "user": "your_username",
    "password": "your_password",
    "table_name": "orders"
}

# Read data from MySQL database
source = SQLDatabaseSource(spark, mysqlSourceConf).read_batch()

# Group data by product category
grouped_data = GroupByTransformer(source, "product_category").transform()

# MySQL database destination configuration
mysqlDestConf = mysqlSourceConf.copy()
mysqlDestConf["table_name"] = "grouped_orders"

# Insert grouped data into a new table
SQLDatabaseDestination(
    data=grouped_data,
    database_url=mysqlDestConf["database_url"],
    user=mysqlDestConf["user"],
    password=mysqlDestConf["password"],
    table_name=mysqlDestConf["table_name"]
).write_batch()
""",

    "q23": "Extract text data from a series of PDF files stored in an SFTP server, perform named entity recognition, and index the entities in an Apache Solr collection.",
    "c23": """
from rtdip_sdk.pipelines.sources import SFTPSource
from rtdip_sdk.pipelines.transformers import NamedEntityRecognitionTransformer
from rtdip_sdk.pipelines.destinations import SolrDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Initialize Spark session
spark = SparkSessionUtility(config={}).execute()

# SFTP server configuration
sftpConf = {
    "host": "sftp.yourserver.com",
    "username": "your_username",
    "password": "your_password",
    "file_path": "/path/to/pdf_files"
}

# Read text data from PDF files
source = SFTPSource(spark, sftpConf).read_batch()

# Perform named entity recognition
entities_data = NamedEntityRecognitionTransformer(source, "text_content").transform()

# Apache Solr destination configuration
solrConf = {
    "solr_url": "http://your_solr_server:8983/solr",
    "collection_name": "entities_collection"
}

# Index entities in Apache Solr
SolrDestination(
    data=entities_data,
    solr_url=solrConf["solr_url"],
    collection_name=solrConf["collection_name"]
).write_batch()
"""
    }
]

