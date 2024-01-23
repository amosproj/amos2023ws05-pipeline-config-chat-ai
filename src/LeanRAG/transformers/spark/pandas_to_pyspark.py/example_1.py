"""
    Converts a Pandas DataFrame to a PySpark DataFrame.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PandasToPySparkTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pandas_to_pyspark = PandasToPySparkTransformer(
        spark=spark,
        df=df,
    )

    result = pandas_to_pyspark.transform()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to convert DataFrame
        df (DataFrame): Pandas DataFrame to be converted
    """