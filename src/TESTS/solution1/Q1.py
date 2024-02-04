#Query 1: I would like to use RTDIP components to read from PythonDeltaSource, transform using BaseRawToMDMTransformer, then write to EVMContractDestination

from rtdip_sdk.pipelines.sources import PythonDeltaSource
from rtdip_sdk.pipelines.transformers import BaseRawToMDMTransformer
from rtdip_sdk.pipelines.destinations import EVMContractDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility

# Not required if using Databricks
spark = SparkSessionUtility(config={}).execute()

# Step 1: Read from PythonDeltaSource
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
data = python_delta_source.read_batch()

# Step 2: Transform using BaseRawToMDMTransformer
miso_to_mdm_transformer = BaseRawToMDMTransformer(
    spark=spark,
    data=data,
    output_type="usage",
    name=None,
    description=None,
    value_type=None,
    version=None,
    series_id=None,
    series_parent_id=None
)
transformed_data = miso_to_mdm_transformer.transform()

# Step 3: Write to EVMContractDestination
evm_contract_destination = EVMContractDestination(
    url="https://polygon-mumbai.g.alchemy.com/v2/⟨API_KEY⟩",
    account="{ACCOUNT-ADDRESS}",
    private_key="{PRIVATE-KEY}",
    abi="{SMART-CONTRACT'S-ABI}",
    contract="{SMART-CONTRACT-ADDRESS}",
    function_name="{SMART-CONTRACT-FUNCTION}",
    function_params=({PARAMETER_1}, {PARAMETER_2}, {PARAMETER_3}),
    transaction={'gas': {GAS}, 'gasPrice': {GAS-PRICE}},
)
evm_contract_destination.write_batch(data=transformed_data)