"""
    Base class for all the Raw to Meters Data Model Transformers.

    Meters Data Model requires two outputs:
        - `UsageData` : To store measurement(value) as timeseries data.
        - `MetaData` : To store meters related meta information.

    It supports the generation of both the outputs as they share some common properties.

    Parameters:
        spark (SparkSession): Spark Session instance.
        data (DataFrame): Dataframe containing the raw MISO data.
        output_type (str): Must be one of `usage` or `meta`.
        name (str): Set this to override default `name` column.
        description (str): Set this to override default `description` column.
        value_type (ValueType): Set this to override default `value_type` column.
        version (str): Set this to override default `version` column.
        series_id (str): Set this to override default `series_id` column.
        series_parent_id (str): Set this to override default `series_parent_id` column.
    """
"""
        Converts a Spark DataFrame structure into new structure based on the Target Schema.

        Returns: Nothing.

        """
"""
        Returns:
            DataFrame: A dataframe with the raw data converted into MDM.
        """