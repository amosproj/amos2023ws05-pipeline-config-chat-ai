
    #Eventhub Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkEventhubDestination
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}


    eventhub_destination = SparkEventhubDestination(
        spark=spark,
        data=df,
        options={
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-EVENTHUB-CONSUMER-GROUP}"
        },
        trigger="10 seconds",
        query_name="EventhubDestination",
        query_wait_interval=None
    )

    eventhub_destination.write_batch()
    