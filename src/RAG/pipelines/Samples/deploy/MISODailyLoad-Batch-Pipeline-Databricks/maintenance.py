from rtdip_sdk.pipelines.utilities import DeltaTableOptimizeUtility, DeltaTableVacuumUtility

def maintenance():
    TABLE_NAMES = [
        "{path.to.table.miso_usage_data}",
        "{path.to.table.miso_meta_data}"
    ]

    for table in TABLE_NAMES:

        DeltaTableOptimizeUtility(
            spark=spark, 
            table_name=table
        ).execute()

        DeltaTableVacuumUtility(
            spark=spark,
            table_name=table
        ).execute()

if __name__ == "__main__":
    maintenance()