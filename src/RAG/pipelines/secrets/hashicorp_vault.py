"""
    Retrieves and creates/updates secrets in a Hashicorp Vault. For more information about Hashicorp Vaults, see [here.](https://developer.hashicorp.com/vault/docs/get-started/developer-qs)

    Example
    -------
    ```python
    # Retrieves Secrets from HashiCorp Vault

    from rtdip_sdk.pipelines.secrets import HashiCorpVaultSecrets

    get_hashicorp_secret = HashiCorpVaultSecrets(
        vault="http://127.0.0.1:8200",
        key="{KEY}",
        secret=None,
        credential="{CREDENTIAL}",
        kwargs=None
    )

    get_hashicorp_secret.get()

    ```
    ```python
    # Creates or Updates Secrets in Hashicorp Vault

    from rtdip_sdk.pipelines.secrets import HashiCorpVaultSecrets

    set_hashicorp_secret = AzureKeyVaultSecrets(
        vault="http://127.0.0.1:8200",
        key="{KEY}",
        secret="{SECRET-TO-BE-SET}",
        credential="{CREDENTIAL}",
        kwargs=None
    )

    set_hashicorp_secret.set()
    ```

    Parameters:
        vault (str): Hashicorp Vault URL
        key (str): Name/Key of the secret in the Hashicorp Vault
        secret (str): Secret or Password to be stored in the Hashicorp Vault
        credential (str): Token for authentication with the Hashicorp Vault
        kwargs (dict): List of additional parameters to be passed when creating a Hashicorp Vault Client. Please see [here](https://hvac.readthedocs.io/en/stable/overview.html#initialize-the-client) for more details on parameters that can be provided to the client
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """
"""
        Retrieves the secret from the Hashicorp Vault
        """
"""
        Creates or updates a secret in the Hashicorp Vault
        """