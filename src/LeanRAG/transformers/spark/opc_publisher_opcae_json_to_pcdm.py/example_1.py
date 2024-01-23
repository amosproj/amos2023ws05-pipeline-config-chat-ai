
    from rtdip_sdk.pipelines.transformers import OPCPublisherOPCAEJsonToPCDMTransformer

    opc_publisher_opcae_json_to_pcdm_transformer = OPCPublisherOPCAEJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX"
        ],
        filter=None
    )

    result = opc_publisher_opcae_json_to_pcdm_transformer.transform()
    