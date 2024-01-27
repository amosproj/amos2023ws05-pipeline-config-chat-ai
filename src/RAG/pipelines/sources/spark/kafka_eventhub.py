"""
    This Spark source class is used to read batch or streaming data from an Eventhub using the Kafka protocol. This enables Eventhubs to be used as a source in applications like Delta Live Tables or Databricks Serverless Jobs as the Spark Eventhubs JAR is not supported in these scenarios.

    The dataframe returned is transformed to ensure the schema is as close to the Eventhub Spark source as possible. There are some minor differences:

    - `offset` is dependent on `x-opt-offset` being populated in the headers provided. If this is not found in the headers, the value will be null
    - `publisher` is dependent on `x-opt-publisher` being populated in the headers provided. If this is not found in the headers, the value will be null
    - `partitionKey` is dependent on `x-opt-partition-key` being populated in the headers provided. If this is not found in the headers, the value will be null
    - `systemProperties` are identified according to the list provided in the [Eventhub documentation](https://learn.microsoft.com/en-us/azure/data-explorer/ingest-data-event-hub-overview#event-system-properties-mapping){ target="_blank" } and [IoT Hub documentation](https://learn.microsoft.com/en-us/azure/data-explorer/ingest-data-iot-hub-overview#event-system-properties-mapping){ target="_blank" }

    Default settings will be specified if not provided in the `options` parameter:

    - `kafka.sasl.mechanism` will be set to `PLAIN`
    - `kafka.security.protocol` will be set to `SASL_SSL`
    - `kafka.request.timeout.ms` will be set to `60000`
    - `kafka.session.timeout.ms` will be set to `60000`

    Examples
    --------
    ```python
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
    ```
    ```python
    #Kafka Source for Batch Queries

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
            "endingOffsets": "latest",
            "failOnDataLoss": "false"
        },
        connection_string=connectionString,
        consumer_group="consumerGroup"
    )

    kafka_eventhub_source.read_batch()
    ```

    Required and optional configurations can be found in the Attributes and Parameter tables below.
    Additionally, there are more optional configurations which can be found [here.](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }

    Parameters:
        spark (SparkSession): Spark Session
        options (dict): A dictionary of Kafka configurations (See Attributes tables below). For more information on configuration options see [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }
        connection_string (str): Eventhubs connection string is required to connect to the Eventhubs service. This must include the Eventhub name as the `EntityPath` parameter. Example `"Endpoint=sb://test.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=test_key;EntityPath=test_eventhub"`
        consumer_group (str): The Eventhub consumer group to use for the connection

    The only configuration that must be set for the Kafka source for both batch and streaming queries is listed below.

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port):  The Kafka "bootstrap.servers" configuration. (Streaming and Batch)

    There are multiple ways of specifying which topics to subscribe to. You should provide only one of these parameters:

    Attributes:
        assign (json string {"topicA"︰[0,1],"topicB"︰[2,4]}):  Specific TopicPartitions to consume. Only one of "assign", "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)
        subscribe (A comma-separated list of topics): The topic list to subscribe. Only one of "assign", "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)
        subscribePattern (Java regex string): The pattern used to subscribe to topic(s). Only one of "assign, "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)

    The following configurations are optional:

    Attributes:
        startingTimestamp (timestamp str): The start point of timestamp when a query is started, a string specifying a starting timestamp for all partitions in topics being subscribed. Please refer the note on starting timestamp offset options below. (Streaming and Batch)
        startingOffsetsByTimestamp (JSON str): The start point of timestamp when a query is started, a json string specifying a starting timestamp for each TopicPartition. Please refer the note on starting timestamp offset options below. (Streaming and Batch)
        startingOffsets ("earliest", "latest" (streaming only), or JSON string): The start point when a query is started, either "earliest" which is from the earliest offsets, "latest" which is just from the latest offsets, or a json string specifying a starting offset for each TopicPartition. In the json, -2 as an offset can be used to refer to earliest, -1 to latest.
        endingTimestamp (timestamp str): The end point when a batch query is ended, a json string specifying an ending timestamp for all partitions in topics being subscribed. Please refer the note on ending timestamp offset options below. (Batch)
        endingOffsetsByTimestamp (JSON str): The end point when a batch query is ended, a json string specifying an ending timestamp for each TopicPartition. Please refer the note on ending timestamp offset options below. (Batch)
        endingOffsets (latest or JSON str): The end point when a batch query is ended, either "latest" which is just referred to the latest, or a json string specifying an ending offset for each TopicPartition. In the json, -1 as an offset can be used to refer to latest, and -2 (earliest) as an offset is not allowed. (Batch)
        maxOffsetsPerTrigger (long): Rate limit on maximum number of offsets processed per trigger interval. The specified total number of offsets will be proportionally split across topicPartitions of different volume. (Streaming)
        minOffsetsPerTrigger (long): Minimum number of offsets to be processed per trigger interval. The specified total number of offsets will be proportionally split across topicPartitions of different volume. (Streaming)
        failOnDataLoss (bool): Whether to fail the query when it's possible that data is lost (e.g., topics are deleted, or offsets are out of range). This may be a false alarm. You can disable it when it doesn't work as you expected.
        minPartitions (int): Desired minimum number of partitions to read from Kafka. By default, Spark has a 1-1 mapping of topicPartitions to Spark partitions consuming from Kafka. (Streaming and Batch)
        includeHeaders (bool): Whether to include the Kafka headers in the row. (Streaming and Batch)

    !!! note "Starting Timestamp Offset Note"
        If Kafka doesn't return the matched offset, the behavior will follow to the value of the option <code>startingOffsetsByTimestampStrategy</code>.

        <code>startingTimestamp</code> takes precedence over <code>startingOffsetsByTimestamp</code> and </code>startingOffsets</code>.

        For streaming queries, this only applies when a new query is started, and that resuming will always pick up from where the query left off. Newly discovered partitions during a query will start at earliest.

    !!! note "Ending Timestamp Offset Note"
        If Kafka doesn't return the matched offset, the offset will be set to latest.

        <code>endingOffsetsByTimestamp</code> takes precedence over <code>endingOffsets</code>.

    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Reads batch data from Kafka.
        """
"""
        Reads streaming data from Kafka.
        """