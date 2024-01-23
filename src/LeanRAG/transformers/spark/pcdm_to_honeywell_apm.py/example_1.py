"""
    Converts a Spark Dataframe in PCDM format to Honeywell APM format.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PCDMToHoneywellAPMTransformer

    pcdm_to_honeywell_apm_transformer = PCDMToHoneywellAPMTransformer(
        data=df,
        quality="Good",
        history_samples_per_message=1,
        compress_payload=True
    )

    result = pcdm_to_honeywell_apm_transformer.transform()
    ```

    Parameters:
        data (Dataframe): Spark Dataframe in PCDM format
        quality (str): Value for quality inside HistorySamples
        history_samples_per_message (int): The number of HistorySamples for each row in the DataFrame (Batch Only)
        compress_payload (bool): If True compresses CloudPlatformEvent with gzip compression
    """