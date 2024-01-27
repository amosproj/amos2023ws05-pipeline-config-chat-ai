"""
    Configures Spark to Connect to an ADLS Gen 2 Storage Account using a Service Principal.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import SparkADLSGen2SPNConnectUtility
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    adls_gen2_connect_utility = SparkADLSGen2SPNConnectUtility(
        spark=spark,
        storage_account="YOUR-STORAGAE-ACCOUNT-NAME",
        tenant_id="YOUR-TENANT-ID",
        client_id="YOUR-CLIENT-ID",
        client_secret="YOUR-CLIENT-SECRET"
    )

    result = adls_gen2_connect_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        storage_account (str): Name of the ADLS Gen 2 Storage Account
        tenant_id (str): Tenant ID of the Service Principal
        client_id (str): Service Principal Client ID
        client_secret (str): Service Principal Client Secret
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """
"""Executes spark configuration to connect to an ADLS Gen 2 Storage Account using a service principal"""