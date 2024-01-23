"""
    Converts a PySpark DataFrame to a Pandas DataFrame.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PySparkToPandasTransformer

    pyspark_to_pandas = PySparkToPandasTransformer(
        df=df
    )

    result = pyspark_to_pandas.transform()
    ```

    Parameters:
        df (DataFrame): PySpark DataFrame to be converted
    """