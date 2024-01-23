
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
    