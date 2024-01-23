
    from rtdip_sdk.pipelines.transformers import EdgeXOPCUAJsonToPCDMTransformer

    edge_opcua_json_to_pcdm_transformer = EdgeXOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert"
    )

    result = edge_opcua_json_to_pcdm_transformer.transform()
    