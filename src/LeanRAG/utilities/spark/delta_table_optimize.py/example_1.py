
    from rtdip_sdk.pipelines.utilities.spark.delta_table_optimize import DeltaTableOptimizeUtility

    table_optimize_utility = DeltaTableOptimizeUtility(
        spark=spark_session,
        table_name="delta_table",
        where="EventDate<=current_date()",
        zorder_by=["EventDate"]
    )

    result = table_optimize_utility.execute()
    