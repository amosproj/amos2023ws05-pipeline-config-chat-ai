"""
    Retrieves secrets from Databricks Secret Scopes. For more information about Databricks Secret Scopes, see [here.](https://docs.databricks.com/security/secrets/secret-scopes.html)

    Example
    -------
    ```python
    # Reads Secrets from Databricks Secret Scopes

    from rtdip_sdk.pipelines.secrets import DatabricksSecrets
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    get_databricks_secret = DatabricksSecrets(
        spark=spark,
        vault="{NAME-OF-DATABRICKS-SECRET-SCOPE}"
        key="{KEY-NAME-OF-SECRET}",
    )

    get_databricks_secret.get()
    ```

    Parameters:
        spark: Spark Session required to read data from a Delta table
        vault: Name of the Databricks Secret Scope
        key: Name/Key of the secret in the Databricks Secret Scope
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK on Databricks
        """
"""
        Retrieves the secret from the Databricks Secret Scope
        """
"""
        Sets the secret in the Secret Scope
        Raises:
            NotImplementedError: Will be implemented at a later point in time
        """