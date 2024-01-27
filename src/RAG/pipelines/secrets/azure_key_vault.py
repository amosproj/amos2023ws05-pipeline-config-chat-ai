"""
    Retrieves and creates/updates secrets in Azure Key Vault. For more information about Azure Key Vaults, see [here.](https://learn.microsoft.com/en-gb/azure/key-vault/general/overview)

    Example
    -------
    ```python
    # Retrieves Secrets from Azure Key Vault

    from rtdip_sdk.pipelines.secrets import AzureKeyVaultSecrets

    get_key_vault_secret = AzureKeyVaultSecrets(
        vault="https://{YOUR-KEY-VAULT}.azure.net/",
        key="{KEY}",
        secret=None,
        credential="{CREDENTIAL}",
        kwargs=None
    )

    get_key_vault_secret.get()

    ```
    ```python
    # Creates or Updates Secrets in Azure Key Vault

    from rtdip_sdk.pipelines.secrets import AzureKeyVaultSecrets

    set_key_vault_secret = AzureKeyVaultSecrets(
        vault="https://{YOUR-KEY-VAULT}.azure.net/",
        key="{KEY}",
        secret="{SECRET-TO-BE-SET}",
        credential="{CREDENTIAL}",
        kwargs=None
    )

    set_key_vault_secret.set()
    ```

    Parameters:
        vault (str): Azure Key Vault URL
        key (str): Key for the secret
        secret (str): Secret or Password to be set in the Azure Key Vault
        credential (str): Credential for authenticating with Azure Key Vault
        kwargs (dict): List of additional parameters to be passed when creating a Azure Key Vault Client. Please see [here](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/keyvault/azure-keyvault-secrets) for more details on parameters that can be provided to the client
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """
"""
        Retrieves the secret from the Azure Key Vault
        """
"""
        Creates or updates a secret in the Azure Key Vault
        """