
    #Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

    delta_destination = SparkDeltaDestination(
        data=df,
        options={
            "overwriteSchema": True
        },
        destination="DELTA-TABLE-PATH",
        mode="append",
        trigger="10 seconds",
        query_name="DeltaDestination",
        query_wait_interval=None
    )

    delta_destination.write_batch()
    