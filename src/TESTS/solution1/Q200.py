#Query 200: I would like to use RTDIP components to read from PythonDeltaSharingSource, transform using BaseRawToMDMTransformer, then write to PythonDeltaDestination
from rtdip_sdk.pipelines.sources import PythonDeltaSharingSource
from rtdip_sdk.pipelines.transformers.spark.base_raw_to_mdm import BaseRawToMDMTransformer
from rtdip_sdk.pipelines.destinations import PythonDeltaDestination

# Read data from PythonDeltaSharingSource
python_delta_sharing_source = PythonDeltaSharingSource(
    profile_path="{CREDENTIAL-FILE-LOCATION}",
    share_name="{SHARE-NAME}",
    schema_name="{SCHEMA-NAME}",
    table_name="{TABLE-NAME}"
)
data = python_delta_sharing_source.read_batch()

# Transform data using BaseRawToMDMTransformer
transformer = BaseRawToMDMTransformer(
    data=data,
    output_type="usage",
    name=None,
    description=None,
    value_type=None,
    version=None,
    series_id=None,
    series_parent_id=None
)
transformed_data = transformer.transform()

# Write transformed data to PythonDeltaDestination
python_delta_destination = PythonDeltaDestination(
    data=transformed_data,
    path="{DELTA-TABLE-PATH}",
    mode="append",
    format_options=None
)
python_delta_destination.write_batch()