"""
    Creates the required Azure Resources for the Databricks Autoloader Notification Mode.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import AzureAutoloaderResourcesUtility

    azure_autoloader_resources_utility = AzureAutoloaderResourcesUtility(
        subscription_id="YOUR-SUBSCRIPTION-ID",
        resource_group_name="YOUR-RESOURCE-GROUP",
        storage_account="YOUR-STORAGE-ACCOUNT-NAME",
        container="YOUR-CONTAINER-NAME",
        directory="DIRECTORY",
        credential="YOUR-CLIENT-ID",
        event_subscription_name="YOUR-EVENT-SUBSCRIPTION",
        queue_name="YOUR-QUEUE-NAME",
        system_topic_name=None
    )

    result = azure_autoloader_resources_utility.execute()
    ```

    Parameters:
        subscription_id (str): Azure Subscription ID
        resource_group_name (str): Resource Group Name of Subscription
        storage_account (str): Storage Account Name
        container (str): Container Name
        directory (str): Directory to be used for filtering messages in the Event Subscription. This will be equivalent to the Databricks Autoloader Path
        credential (TokenCredential): Credentials to authenticate with Storage Account
        event_subscription_name (str): Name of the Event Subscription
        queue_name (str): Name of the queue that will be used for the Endpoint of the Messages
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """