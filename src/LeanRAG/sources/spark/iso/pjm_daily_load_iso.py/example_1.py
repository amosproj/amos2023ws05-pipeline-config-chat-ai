
    from rtdip_sdk.pipelines.sources import PJMDailyLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_source = PJMDailyLoadISOSource(
        spark=spark,
        options={
            "api_key": "{api_key}",
            "load_type": "actual"
        }
    )

    pjm_source.read_batch()
    