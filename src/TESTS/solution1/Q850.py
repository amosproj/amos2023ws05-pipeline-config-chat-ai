#Query 850: I would like to use RTDIP components to read from SparkDeltaSharingSource, transform using OPCPublisherOPCUAJsonToPCDMTransformer, then write to SparkDeltaDestination
from rtdip_sdk.pipelines.sources import SparkDeltaSharingSource
from rtdip_sdk.pipelines.transformers import OPCPublisherOPCUAJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# Read from SparkDeltaSharingSource
delta_sharing_source = SparkDeltaSharingSource(
    spark=spark,
    options={
        "startingVersion": 0
    },
    table_name="{YOUR-DELTA-TABLE-PATH}"
)
df = delta_sharing_source.read_stream()

# Transform using OPCPublisherOPCUAJsonToPCDMTransformer
opc_publisher_opcua_json_to_pcdm_transformer = OPCPublisherOPCUAJsonToPCDMTransformer(
    data=df,
    source_column_name="body",
    multiple_rows_per_message=True,
    status_null_value="Good",
    change_type_value="insert",
    timestamp_formats=[
        "yyyy-MM-dd'T'HH:mm:ss.SSSX",
        "yyyy-MM-dd'T'HH:mm:ssX"
    ],
    filter=None
)
df_transformed = opc_publisher_opcua_json_to_pcdm_transformer.transform()

# Write to SparkDeltaDestination
delta_destination = SparkDeltaDestination(
    data=df_transformed,
    options={
        "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
    },
    destination_table="{DELTA-TABLE-PATH}",
    mode="append",
    trigger="10 seconds",
    query_name="PCDMToDeltaDestination",
    query_wait_interval=None,
    merge=True,
    try_broadcast_join=False,
    remove_nanoseconds=False,
    remove_duplicates=True
)
delta_destination.write_stream()