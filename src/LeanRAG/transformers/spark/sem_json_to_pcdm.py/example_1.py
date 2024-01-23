
    from rtdip_sdk.pipelines.transformers import SEMJsonToPCDMTransformer

    sem_json_to_pcdm_transformer = SEMJsonToPCDMTransformer(
        data=df
        source_column_name="body",
        version=10,
        status_null_value="Good",
        change_type_value="insert"
    )

    result = sem_json_to_pcdm_transformer.transform()
    