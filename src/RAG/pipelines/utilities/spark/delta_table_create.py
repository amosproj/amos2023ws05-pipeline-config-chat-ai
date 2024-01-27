"""
    Creates a Delta Table in a Hive Metastore or in Databricks Unity Catalog.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.utilities.spark.delta_table_create import DeltaTableCreateUtility, DeltaTableColumn

    table_create_utility = DeltaTableCreateUtility(
        spark=spark_session,
        table_name="delta_table",
        columns=[
            DeltaTableColumn(name="EventDate", type="date", nullable=False, metadata={"delta.generationExpression": "CAST(EventTime AS DATE)"}),
            DeltaTableColumn(name="TagName", type="string", nullable=False),
            DeltaTableColumn(name="EventTime", type="timestamp", nullable=False),
            DeltaTableColumn(name="Status", type="string", nullable=True),
            DeltaTableColumn(name="Value", type="float", nullable=True)
        ],
        partitioned_by=["EventDate"],
        properties={"delta.logRetentionDuration": "7 days", "delta.enableChangeDataFeed": "true"},
        comment="Creation of Delta Table"
    )

    result = table_create_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        table_name (str): Name of the table, including catalog and schema if table is to be created in Unity Catalog
        columns (list[DeltaTableColumn]): List of columns and their related column properties
        partitioned_by (list[str], optional): List of column names to partition the table by
        location (str, optional): Path to storage location
        properties (dict, optional): Propoerties that can be specified for a Delta Table. Further information on the options available are [here](https://docs.databricks.com/delta/table-properties.html#delta-table-properties)
        comment (str, optional): Provides a comment on the table metadata


    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """