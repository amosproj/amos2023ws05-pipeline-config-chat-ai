"""
    This Spark Destination class is used to write batch or streaming data to an Eventhub using the Kafka protocol. This enables Eventhubs to be used as a destination in applications like Delta Live Tables or Databricks Serverless Jobs as the Spark Eventhubs JAR is not supported in these scenarios.

    Default settings will be specified if not provided in the `options` parameter:

    - `kafka.sasl.mechanism` will be set to `PLAIN`
    - `kafka.security.protocol` will be set to `SASL_SSL`
    - `kafka.request.timeout.ms` will be set to `60000`
    - `kafka.session.timeout.ms` will be set to `60000`

    Example
    --------
    ```python
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
    ```

    Parameters:
        spark (SparkSession): Spark Session
        data (DataFrame): Any columns not listed in the required schema [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html#writing-data-to-kafka){ target="_blank" } will be merged into a single column named "value", or ignored if "value" is an existing column
        connection_string (str): Eventhubs connection string is required to connect to the Eventhubs service. This must include the Eventhub name as the `EntityPath` parameter. Example `"Endpoint=sb://test.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=test_key;EntityPath=test_eventhub"`
        options (dict): A dictionary of Kafka configurations (See Attributes tables below)
        consumer_group (str): The Eventhub consumer group to use for the connection
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (optional str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    The following are commonly used parameters that may be included in the options dict. kafka.bootstrap.servers is the only required config. A full list of configs can be found [here](https://kafka.apache.org/documentation/#producerconfigs){ target="_blank" }

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port):  The Kafka "bootstrap.servers" configuration. (Streaming and Batch)
        topic (string): Required if there is no existing topic column in your DataFrame. Sets the topic that all rows will be written to in Kafka. (Streaming and Batch)
        includeHeaders (bool): Determines whether to include the Kafka headers in the row; defaults to False. (Streaming and Batch)
    """