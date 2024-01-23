
    from rtdip_sdk.pipelines.transformers import SSIPPIJsonStreamToPCDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    ssip_pi_json_stream_to_pcdm_transformer = SSIPPIJsonStreamToPCDMTransformer(
        spark=spark,
        data=df,
        source_column_name="body",
        properties_column_name="",
        metadata_delta_table=None
    )

    result = ssip_pi_json_stream_to_pcdm_transformer.transform()
    