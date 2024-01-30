#Query 70: I would like to use RTDIP components to read from PythonDeltaSource, transform using PandasToPySparkTransformer, then write to SparkDeltaMergeDestination
from rtdip_sdk.pipelines.sources import PythonDeltaSource
from rtdip_sdk.pipelines.transformers import PandasToPySparkTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaMergeDestination

# Read data from PythonDeltaSource
python_delta_source = PythonDeltaSource(
    path="YOUR_DELTA_TABLE_PATH",
    version=None,
    storage_options={
        "azure_storage_account_name": "YOUR_STORAGE_ACCOUNT_NAME",
        "azure_storage_account_key": "YOUR_STORAGE_ACCOUNT_KEY"
    },
    pyarrow_options=None,
    without_files=False
)
df = python_delta_source.read_batch()

# Transform the data using PandasToPySparkTransformer
transformer = PandasToPySparkTransformer()
transformed_df = transformer.transform(df)

# Write the transformed data to SparkDeltaMergeDestination
delta_merge_destination = SparkDeltaMergeDestination(
    data=transformed_df,
    destination="YOUR_DELTA_TABLE_PATH",
    options={},
    merge_condition="`source.id = target.id`",
    when_matched_update_list=None,
    when_matched_delete_list=None,
    when_not_matched_insert_list=None,
    when_not_matched_by_source_update_list=None,
    when_not_matched_by_source_delete_list=None,
    try_broadcast_join=False,
    trigger="10 seconds",
    query_name="DeltaDestination",
    query_wait_interval=None
)
delta_merge_destination.write_batch()