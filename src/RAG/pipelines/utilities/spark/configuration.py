"""
    Sets configuration key value pairs to a Spark Session

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import SparkConfigurationUtility
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    configuration_utility = SparkConfigurationUtility(
        spark=spark,
        config={}
    )

    result = configuration_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        config (dict): Dictionary of spark configuration to be applied to the spark session
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""Executes configuration key value pairs to a Spark Session"""