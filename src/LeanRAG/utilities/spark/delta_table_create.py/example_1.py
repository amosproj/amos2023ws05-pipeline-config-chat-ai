
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
    