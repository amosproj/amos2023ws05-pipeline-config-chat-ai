"""
    Creates or Gets a Spark Session and uses settings and libraries of the imported RTDIP components to populate the spark configuration and jars in the spark session.

    Call this component after all imports of the RTDIP components to ensure that the spark session is configured correctly.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    spark_session_utility = SparkSessionUtility(
        config={},
        module=None,
        remote=None
    )

    result = spark_session_utility.execute()
    ```

    Parameters:
        config (optional dict): Dictionary of spark configuration to be applied to the spark session
        module (optional str): Provide the module to use for imports of rtdip-sdk components. If not populated, it will use the calling module to check for imports
        remote (optional str): Specify the remote parameters if intending to use Spark Connect
    """