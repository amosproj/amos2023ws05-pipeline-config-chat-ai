
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
    