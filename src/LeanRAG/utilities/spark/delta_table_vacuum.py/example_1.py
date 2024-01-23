"""
    [Vacuums](https://docs.delta.io/latest/delta-utility.html#-delta-vacuum) a Delta Table.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.utilities.spark.delta_table_vacuum import DeltaTableVacuumUtility

    table_vacuum_utility =  DeltaTableVacuumUtility(
        spark=spark_session,
        table_name="delta_table",
        retention_hours="168"
    )

    result = table_vacuum_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        table_name (str): Name of the table, including catalog and schema if table is to be created in Unity Catalog
        retention_hours (int, optional): Sets the retention threshold in hours.
    """