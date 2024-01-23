
    from rtdip_sdk.pipelines.sources import SparkConfigurationUtility
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    configuration_utility = SparkConfigurationUtility(
        spark=spark,
        config={}
    )

    result = configuration_utility.execute()
    