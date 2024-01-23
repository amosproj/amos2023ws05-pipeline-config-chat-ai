
    from rtdip_sdk.pipelines.destinations import SparkKafkaEventhubDestination
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}

    eventhub_destination = SparkKafkaEventhubDestination(
        spark=spark,
        data=df,
        options={
            "kafka.bootstrap.servers": "host1:port1,host2:port2"
        },
        consumer_group="{YOUR-EVENTHUB-CONSUMER-GROUP}",
        trigger="10 seconds",
        query_name="KafkaEventhubDestination",
        query_wait_interval=None
    )

    eventhub_destination.write_stream()

    OR

    eventhub_destination.write_batch()
    