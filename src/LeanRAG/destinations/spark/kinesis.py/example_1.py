"""
    This Kinesis destination class is used to write batch or streaming data to Kinesis. Kinesis configurations need to be specified as options in a dictionary.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.destinations import SparkKinesisDestination

    kinesis_destination = SparkKinesisDestination(
        data=df,
        options={
            "endpointUrl": "https://kinesis.{REGION}.amazonaws.com",
            "awsAccessKey": "{YOUR-AWS-ACCESS-KEY}",
            "awsSecretKey": "{YOUR-AWS-SECRET-KEY}",
            "streamName": "{YOUR-STREAM-NAME}"
        },
        mode="update",
        trigger="10 seconds",
        query_name="KinesisDestination",
        query_wait_interval=None
    )

    kinesis_destination.write_stream()

    OR

    kinesis_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be written to Delta
        options (dict): A dictionary of Kinesis configurations (See Attributes table below). All Configuration options for Kinesis can be found [here.](https://github.com/qubole/kinesis-sql#kinesis-sink-configuration){ target="_blank" }
        mode (str): Method of writing to Kinesis - append, complete, update
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        endpointUrl (str): Endpoint of the kinesis stream.
        awsAccessKey (str): AWS access key.
        awsSecretKey (str): AWS secret access key corresponding to the access key.
        streamName (List[str]): Name of the streams in Kinesis to write to.
    """