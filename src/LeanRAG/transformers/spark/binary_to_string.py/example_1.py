"""
    Converts a dataframe body column from a binary to a string.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import BinaryToStringTransformer

    binary_to_string_transformer = BinaryToStringTransformer(
        data=df,
        souce_column_name="body",
        target_column_name="body"
    )

    result = binary_to_string_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe to be transformed
        source_column_name (str): Spark Dataframe column containing the Binary data
        target_column_name (str): Spark Dataframe column name to be used for the String data
    """