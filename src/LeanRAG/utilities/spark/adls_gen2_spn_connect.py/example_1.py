
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
    