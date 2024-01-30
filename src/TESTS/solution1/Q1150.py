#Query 1150: I would like to use RTDIP components to read from SparkEventhubSource, transform using ECMWFExtractPointToWeatherDataModel, then write to SparkKafkaDestination

####### solution 
#I'm sorry, but I don't have access to the specific implementation details for the ECMWFExtractPointToWeatherDataModel transformer. You will need to refer to the documentation or contact the developer of that specific transformer for more information on how to configure and use it in your code.
from rtdip_sdk.pipelines.sources import SparkEventhubSource
from rtdip_sdk.pipelines.transformers import ECMWFExtractPointToWeatherDataModel
from rtdip_sdk.pipelines.destinations import SparkKafkaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# Configure the SparkEventhubSource
connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
consumerGroup = "{YOUR-CONSUMER-GROUP}"

eventhub_source = SparkEventhubSource(
    spark=spark,
    options={
        "startingOffsets": "earliest",
        "maxOffsetsPerTrigger": 10000,
        "failOnDataLoss": "false",
    },
    connection_string=connectionString,
    consumer_group=consumerGroup
)

# Configure the ECMWFExtractPointToWeatherDataModel transformer
ecmwf_extractor = ECMWFExtractPointToWeatherDataModel(
    data=eventhub_source.read_stream(),
    source_column_name="value",
    latitude_column_name="latitude",
    longitude_column_name="longitude",
    timestamp_column_name="timestamp",
    value_column_name="value"
)

# Configure the SparkKafkaDestination
kafka_bootstrap_servers = "{KAFKA-BOOTSTRAP-SERVERS}"
kafka_topic = "{KAFKA-TOPIC}"

kafka_destination = SparkKafkaDestination(
    data=ecmwf_extractor.transform(),
    options={
        "kafka.bootstrap.servers": kafka_bootstrap_servers
    },
    topic=kafka_topic
)

kafka_destination.write_stream()