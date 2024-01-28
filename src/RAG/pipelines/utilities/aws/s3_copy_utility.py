"""
    Copies an object from S3 to S3, from Local to S3 and S3 to local depending on the source and destination uri.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import S3CopyUtility

    s3_copy_utility = S3CopyUtility(
        source_uri="YOUR-SOURCE-URI",
        destination_uri="YOUR-DESTINATION-URI",
        source_version_id="YOUR-VERSION-ID",
        extra_args={},
        callback="YOUD-SID",
        source_client="PRINCIPAL",
        transfer_config=["ACTIONS"]
    )

    result = s3_bucket_policy_utility.execute()
    ```

    Parameters:
        source_uri (str): URI of the source object
        destination_uri (str): URI of the destination object
        source_version_id (optional str): Version ID of the source bucket
        extra_args (optional dict): Extra arguments that can be passed to the client operation. See [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.S3Transfer.ALLOWED_DOWNLOAD_ARGS){ target="_blank" } for a list of download arguments
        callback (optional function): Takes a UDF used for tracking the progress of the copy operation
        source_client (optional botocore or boto3 client): A different S3 client to use for the source bucket during the copy operation
        transfer_config (optional class): The transfer configuration used during the copy. See [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig){ target="_blank" } for all parameters

    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """