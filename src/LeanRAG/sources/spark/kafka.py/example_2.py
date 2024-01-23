
     #Kafka Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkKafkaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    kafka_source = SparkKafkaSource(
        spark=spark,
        options={
            "kafka.bootstrap.servers": "{HOST_1}:{PORT_1},{HOST_2}:{PORT_2}",
            "subscribe": "{TOPIC_1},{TOPIC_2}",
            "startingOffsets": "earliest",
            "endingOffsets": "latest"
        }
    )

    kafka_source.read_batch()
    