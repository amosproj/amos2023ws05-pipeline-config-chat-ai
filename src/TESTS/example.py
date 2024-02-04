from rtdip_sdk.pipelines.sources import PythonDeltaSharingSource
from rtdip_sdk.pipelines.transformers import SSIPPIBinaryFileToPCDMTransformer
from rtdip_sdk.pipelines.destinations import SparkEventhubDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# Step 1: Read from PythonDeltaSharingSource
python_delta_sharing_source = PythonDeltaSharingSource(
    profile_path="{CREDENTIAL-FILE-LOCATION}",
    share_name="{SHARE-NAME}",
    schema_name="{SCHEMA-NAME}",
    table_name="{TABLE-NAME}"
)

df = python_delta_sharing_source.read_batch()

# Step 2: Transform using SSIPPIBinaryFileToPCDMTransformer
ssip_pi_binary_file_to_pcdm_transformer = SSIPPIBinaryFileToPCDMTransformer(
    spark=spark,
    data=df,
    source_column_name="{SOURCE-COLUMN-NAME}",
    properties_column_name="{PROPERTIES-COLUMN-NAME}",
    metadata_delta_table="{METADATA-DELTA-TABLE}"
)

transformed_df = ssip_pi_binary_file_to_pcdm_transformer.transform()

# Step 3: Write to SparkEventhubDestination
spark_eventhub_destination = SparkEventhubDestination(
    data=transformed_df,
    connection_string="Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
)

spark_eventhub_destination.write_batch()