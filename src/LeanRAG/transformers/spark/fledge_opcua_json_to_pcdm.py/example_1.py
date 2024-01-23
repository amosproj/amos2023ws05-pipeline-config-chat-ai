
    from rtdip_sdk.pipelines.transformers import FledgeOPCUAJsonToPCDMTransformer

    fledge_opcua_json_to_pcdm_transfromer = FledgeOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX",
        ]
    )

    result = fledge_opcua_json_to_pcdm_transfromer.transform()
    