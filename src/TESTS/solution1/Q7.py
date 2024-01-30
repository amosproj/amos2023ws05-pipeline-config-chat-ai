#Query 7: I would like to use RTDIP components to read from PythonDeltaSource, transform using BaseRawToMDMTransformer, then write to SparkKafkaEventhubDestination
from rtdip_sdk.pipelines.sources import PythonDeltaSource
from rtdip_sdk.pipelines.transformers.spark.base_raw_to_mdm import BaseRawToMDMTransformer
from rtdip_sdk.pipelines.destinations import SparkKafkaEventhubDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Read from PythonDeltaSource
path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}"
python_delta_source = PythonDeltaSource(
    path=path,
    version=None,
    storage_options={
        "azure_storage_account_name": "{AZURE-STORAGE-ACCOUNT-NAME}",
        "azure_storage_account_key": "{AZURE-STORAGE-ACCOUNT-KEY}"
    },
    pyarrow_options=None,
    without_files=False
)
df = python_delta_source.read_batch()

# Transform using BaseRawToMDMTransformer
spark = SparkSessionUtility(config={}).execute()
base_raw_to_mdm_transformer = BaseRawToMDMTransformer(
    spark=spark,
    data=df,
    output_type="usage",
    name=None,
    description=None,
    value_type=None,
    version=None,
    series_id=None,
    series_parent_id=None
)
transformed_df = base_raw_to_mdm_transformer.transform()

# Write to SparkKafkaEventhubDestination
connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
eventhub_destination = SparkKafkaEventhubDestination(
    data=transformed_df,
    options={
        "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
    },
    connection_string=connectionString,
    topic="{EVENT_HUB_TOPIC}",
    mode="append",
    trigger="10 seconds",
    query_name="KafkaEventhubDestination",
    query_wait_interval=None
)
eventhub_destination.write_stream()