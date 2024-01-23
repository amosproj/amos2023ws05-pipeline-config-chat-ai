
    from rtdip_sdk.pipelines.transformers import BinaryToStringTransformer

    binary_to_string_transformer = BinaryToStringTransformer(
        data=df,
        souce_column_name="body",
        target_column_name="body"
    )

    result = binary_to_string_transformer.transform()
    