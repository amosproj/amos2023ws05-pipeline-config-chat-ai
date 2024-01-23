
    #Kafka Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkKafkaEventhubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
    consumerGroup = "{YOUR-CONSUMER-GROUP}"

    kafka_eventhub_source = SparkKafkaEventhubSource(
        spark=spark,
        options={
            "startingOffsets": "earliest",
            "maxOffsetsPerTrigger": 10000,
            "failOnDataLoss": "false",
        },
        connection_string=connectionString,
        consumer_group="consumerGroup"
    )

    kafka_eventhub_source.read_stream()
    