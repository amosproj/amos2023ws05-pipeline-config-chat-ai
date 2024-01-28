"""
    This Spark destination class is used to write batch or streaming data from Kafka. Required and optional configurations can be found in the Attributes tables below.

    Additionally, there are more optional configurations which can be found [here.](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }

    For compatibility between Spark and Kafka, the columns in the input dataframe are concatenated into one 'value' column of JSON string.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.destinations import SparkKafkaDestination

    kafka_destination = SparkKafkaDestination(
        data=df,
        options={
            "kafka.bootstrap.servers": "host1:port1,host2:port2"
        },
        trigger="10 seconds",
        query_name="KafkaDestination",
        query_wait_interval=None
    )

    kafka_destination.write_stream()

    OR

    kafka_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be written to Kafka
        options (dict): A dictionary of Kafka configurations (See Attributes tables below). For more information on configuration options see [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    The following options must be set for the Kafka destination for both batch and streaming queries.

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port): The Kafka "bootstrap.servers" configuration. (Streaming and Batch)

    The following configurations are optional:

    Attributes:
        topic (str):Sets the topic that all rows will be written to in Kafka. This option overrides any topic column that may exist in the data. (Streaming and Batch)
        includeHeaders (bool): Whether to include the Kafka headers in the row. (Streaming and Batch)

    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""
        Writes batch data to Kafka.
        """
"""
        Writes steaming data to Kafka.
        """