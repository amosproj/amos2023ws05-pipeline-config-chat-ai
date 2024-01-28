"""
    This Spark destination class is used to write batch or streaming data to Eventhubs. Eventhub configurations need to be specified as options in a dictionary.
    Additionally, there are more optional configurations which can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
    If using startingPosition or endingPosition make sure to check out **Event Position** section for more details and examples.

    Examples
    --------
    ```python
    #Eventhub Destination for Streaming Queries

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
            "eventhubs.consumerGroup": "{YOUR-EVENTHUB-CONSUMER-GROUP}",
            "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
        },
        trigger="10 seconds",
        query_name="EventhubDestination",
        query_wait_interval=None
    )

    eventhub_destination.write_stream()
    ```
    ```python
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
    ```

    Parameters:
        spark (SparkSession): Spark Session
        data (DataFrame): Dataframe to be written to Eventhub
        options (dict): A dictionary of Eventhub configurations (See Attributes table below). All Configuration options for Eventhubs can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
        eventhubs.connectionString (str):  Eventhubs connection string is required to connect to the Eventhubs service. (Streaming and Batch)
        eventhubs.consumerGroup (str): A consumer group is a view of an entire eventhub. Consumer groups enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their own offsets. (Streaming and Batch)
        eventhubs.startingPosition (JSON str): The starting position for your Structured Streaming job. If a specific EventPosition is not set for a partition using startingPositions, then we use the EventPosition set in startingPosition. If nothing is set in either option, we will begin consuming from the end of the partition. (Streaming and Batch)
        eventhubs.endingPosition: (JSON str): The ending position of a batch query. This works the same as startingPosition. (Batch)
        maxEventsPerTrigger (long): Rate limit on maximum number of events processed per trigger interval. The specified total number of events will be proportionally split across partitions of different volume. (Stream)
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Writes batch data to Eventhubs.
        """
"""
        Writes steaming data to Eventhubs.
        """