
    from rtdip_sdk.pipelines.transformers import PandasToPySparkTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pandas_to_pyspark = PandasToPySparkTransformer(
        spark=spark,
        df=df,
    )

    result = pandas_to_pyspark.transform()
    