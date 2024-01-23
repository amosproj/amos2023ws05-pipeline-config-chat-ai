
    from rtdip_sdk.pipelines.transformers import MiricoJsonToPCDMTransformer

    mirico_json_to_pcdm_transformer = MiricoJsonToPCDMTransformer(
        data=df
        source_column_name="body",
        status_null_value="Good",
        change_type_value="insert"
    )

    result = mirico_json_to_pcdm_transformer.transform()
    