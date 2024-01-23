
    #Rest API Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkRestAPIDestination

    rest_api_destination = SparkRestAPIDestination(
        data=df,
        options={
            "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
        },
        url="{REST-API-URL}",
        headers = {
            'Authorization': 'Bearer {}'.format("{TOKEN}")
        },
        batch_size=100,
        method="POST",
        parallelism=8,
        trigger="1 minute",
        query_name="DeltaRestAPIDestination",
        query_wait_interval=None
    )

    rest_api_destination.write_stream()
    