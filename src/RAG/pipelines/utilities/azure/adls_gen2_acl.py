"""
    Assigns Azure AD Groups to ACLs on directories in an Azure Data Lake Store Gen 2 storage account.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import ADLSGen2DirectoryACLUtility

    adls_gen2_directory_acl_utility = ADLSGen2DirectoryACLUtility(
        storage_account="YOUR-STORAGAE-ACCOUNT-NAME",
        container="YOUR-ADLS_CONTAINER_NAME",
        credential="YOUR-TOKEN-CREDENTIAL",
        directory="DIRECTORY",
        group_object_id="GROUP-OBJECT",
        folder_permissions="r-x",
        parent_folder_permissions="r-x",
        root_folder_permissions="r-x",
        set_as_default_acl=True,
        create_directory_if_not_exists=True
    )

    result = adls_gen2_directory_acl_utility.execute()
    ```

    Parameters:
        storage_account (str): ADLS Gen 2 Storage Account Name
        container (str): ADLS Gen 2 Container Name
        credential (TokenCredential): Credentials to authenticate with ADLS Gen 2 Storage Account
        directory (str): Directory to be assign ACLS to in an ADLS Gen 2
        group_object_id (str): Azure AD Group Object ID to be assigned to Directory
        folder_permissions (optional, str): Folder Permissions to Assign to directory
        parent_folder_permissions (optional, str): Folder Permissions to Assign to parent directories. Parent Folder ACLs not set if None
        root_folder_permissions (optional, str): Folder Permissions to Assign to root directory. Root Folder ACL not set if None
        set_as_default_acl (bool, optional): Sets the ACL as the default ACL on the folder
        create_directory_if_not_exists (bool, optional): Creates the directory(and Parent Directories) if it does not exist
    """
"""
        Attributes:
            SystemType (Environment): Requires PYTHON
        """