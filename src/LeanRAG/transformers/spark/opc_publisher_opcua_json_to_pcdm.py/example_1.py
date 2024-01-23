
    from rtdip_sdk.pipelines.transformers import OPCPublisherOPCUAJsonToPCDMTransformer

    opc_publisher_opcua_json_to_pcdm_transformer = OPCPublisherOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        multiple_rows_per_message=True,
        status_null_value="Good",
        change_type_value="insert",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX"
        ],
        filter=None
    )

    result = opc_publisher_opcua_json_to_pcdm_transformer.transform()
    