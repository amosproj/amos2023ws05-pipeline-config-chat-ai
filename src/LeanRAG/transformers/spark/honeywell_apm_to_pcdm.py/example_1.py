
    from rtdip_sdk.pipelines.transformers import HoneywellAPMJsonToPCDMTransformer

    honeywell_apm_json_to_pcdm_transformer = HoneywellAPMJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert"
    )

    result = honeywell_apm_json_to_pcdm_transformer.transform()
    