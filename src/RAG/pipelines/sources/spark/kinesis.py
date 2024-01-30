"""
    The Spark Kinesis Source is used to read data from Kinesis in a Databricks environment.
    Structured streaming from Kinesis is **not** supported in open source Spark.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import SparkKinesisSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    kinesis_source = SparkKinesisSource(
        spark=spark,
        options={
            "awsAccessKey": "{AWS-ACCESS-KEY}",
            "awsSecretKey": "{AWS-SECRET-KEY}",
            "streamName": "{STREAM-NAME}",
            "region": "{REGION}",
            "endpoint": "https://kinesis.{REGION}.amazonaws.com",
            "initialPosition": "earliest"
        }
    )

    kinesis_source.read_stream()

    OR

    kinesis_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from Kinesis
        options (dict): Options that can be specified for a Kinesis read operation (See Attributes table below). Further information on the options is available [here](https://docs.databricks.com/structured-streaming/kinesis.html#configuration){ target="_blank" }

    Attributes:
        awsAccessKey (str): AWS access key.
        awsSecretKey (str): AWS secret access key corresponding to the access key.
        streamName (List[str]): The stream names to subscribe to.
        region (str): The region the streams are defined in.
        endpoint (str): The regional endpoint for Kinesis Data Streams.
        initialPosition (str): The point to start reading from; earliest, latest, or at_timestamp.
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK_DATABRICKS
        """
"""
        Raises:
            NotImplementedError: Kinesis only supports streaming reads. To perform a batch read, use the read_stream method of this component and specify the Trigger on the write_stream to be `availableNow=True` to perform batch-like reads of cloud storage files.
        """
"""
        Reads streaming data from Kinesis. All of the data in the table is processed as well as any new data that arrives after the stream started.
        """