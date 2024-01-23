
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
    