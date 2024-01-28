"""
    [Optimizes](https://docs.delta.io/latest/optimizations-oss.html) a Delta Table.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.utilities.spark.delta_table_optimize import DeltaTableOptimizeUtility

    table_optimize_utility = DeltaTableOptimizeUtility(
        spark=spark_session,
        table_name="delta_table",
        where="EventDate<=current_date()",
        zorder_by=["EventDate"]
    )

    result = table_optimize_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        table_name (str): Name of the table, including catalog and schema if table is to be created in Unity Catalog
        where (str, optional): Apply a partition filter to limit optimize to specific partitions. Example, "date='2021-11-18'" or "EventDate<=current_date()"
        zorder_by (list[str], optional): List of column names to zorder the table by. For more information, see [here.](https://docs.delta.io/latest/optimizations-oss.html#optimize-performance-with-file-management&language-python)
    """
"""
        Attributes:
            SystemType (Environment): Requires PYSPARK
        """