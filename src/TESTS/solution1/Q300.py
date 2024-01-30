#Query 300: I would like to use RTDIP components to read from PythonDeltaSharingSource, transform using SEMJsonToPCDMTransformer, then write to SparkDeltaDestination
from rtdip_sdk.pipelines.sources import PythonDeltaSharingSource
from rtdip_sdk.pipelines.transformers import SEMJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

# Create Delta Sharing Source
python_delta_sharing_source = PythonDeltaSharingSource(
    profile_path="{CREDENTIAL-FILE-LOCATION}",
    share_name="{SHARE-NAME}",
    schema_name="{SCHEMA-NAME}",
    table_name="{TABLE-NAME}"
)

# Read data from Delta Sharing Source
df = python_delta_sharing_source.read_batch()

# Create SEMJsonToPCDMTransformer
sem_json_to_pcdm_transformer = SEMJsonToPCDMTransformer(
    data=df,
    source_column_name="{SOURCE-COLUMN-NAME}",
    version={VERSION},
    status_null_value="{STATUS-NULL-VALUE}",
    change_type_value="{CHANGE-TYPE-VALUE}"
)

# Transform data to PCDM
transformed_df = sem_json_to_pcdm_transformer.transform()

# Create SparkDeltaDestination
spark_delta_destination = SparkDeltaDestination(
    data=transformed_df,
    destination_path="{DELTA-TABLE-PATH}",
    mode="{MODE}",
    partition_column="{PARTITION-COLUMN}",
    partition_by="{PARTITION-BY}",
    save_mode="{SAVE-MODE}"
)

# Write data to Delta table
spark_delta_destination.write_batch()