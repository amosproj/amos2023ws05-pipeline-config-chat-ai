
    from rtdip_sdk.pipelines.transformers import SSIPPIBinaryFileToPCDMTransformer

    ssip_pi_binary_file_to_pcdm_transformer = SSIPPIBinaryFileToPCDMTransformer(
        data=df
    )

    result = ssip_pi_binary_file_to_pcdm_transformer.transform()
    