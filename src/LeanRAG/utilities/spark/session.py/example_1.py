
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    spark_session_utility = SparkSessionUtility(
        config={},
        module=None,
        remote=None
    )

    result = spark_session_utility.execute()
    