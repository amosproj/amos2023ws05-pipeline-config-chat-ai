
    from rtdip_sdk.pipelines.utilities.spark.delta_table_vacuum import DeltaTableVacuumUtility

    table_vacuum_utility =  DeltaTableVacuumUtility(
        spark=spark_session,
        table_name="delta_table",
        retention_hours="168"
    )

    result = table_vacuum_utility.execute()
    