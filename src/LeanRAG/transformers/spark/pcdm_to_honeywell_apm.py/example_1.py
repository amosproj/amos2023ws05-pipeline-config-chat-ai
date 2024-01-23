
    from rtdip_sdk.pipelines.transformers import PCDMToHoneywellAPMTransformer

    pcdm_to_honeywell_apm_transformer = PCDMToHoneywellAPMTransformer(
        data=df,
        quality="Good",
        history_samples_per_message=1,
        compress_payload=True
    )

    result = pcdm_to_honeywell_apm_transformer.transform()
    