
    from rtdip_sdk.pipelines.sources import MISODailyLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_source = MISODailyLoadISOSource(
        spark=spark,
        options={
            "load_type": "actual",
            "date": "20230520",
        }
    )

    miso_source.read_batch()
    