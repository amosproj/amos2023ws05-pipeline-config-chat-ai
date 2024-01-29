"""
    Assigns an IAM Bucket Policy to an S3 Bucket.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import S3BucketPolicyUtility

    s3_bucket_policy_utility = S3BucketPolicyUtility(
        bucket_name="YOUR-BUCKET-NAME",
        aws_access_key_id="YOUR-AWS-ACCESS-KEY",
        aws_secret_access_key="YOUR-AWS-SECRET-ACCESS-KEY",
        aws_session_token="YOUR-AWS-SESSION-TOKEN",
        sid="YOUD-SID",
        effect="EFFECT",
        principal="PRINCIPAL",
        action=["ACTIONS"],
        resource=["RESOURCES"]
    )

    result = s3_bucket_policy_utility.execute()
    ```

    Parameters:
        bucket_name (str): S3 Bucket Name
        aws_access_key_id (str): AWS Access Key
        aws_secret_access_key (str): AWS Secret Key
        aws_session_token (str): AWS Session Token
        sid (str): S3 Bucket Policy Sid to be updated
        effect (str): Effect to be applied to the policy
        principal (str): Principal to be applied to Policy
        action (list[str]): List of actions to be applied to the policy
        resource (list[str]): List of resources to be applied to the policy
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """