
    from rtdip_sdk.pipelines.transformers import PySparkToPandasTransformer

    pyspark_to_pandas = PySparkToPandasTransformer(
        df=df
    )

    result = pyspark_to_pandas.transform()
    