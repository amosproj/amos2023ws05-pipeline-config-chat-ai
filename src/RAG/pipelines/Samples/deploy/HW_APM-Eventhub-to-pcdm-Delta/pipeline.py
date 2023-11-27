from rtdip_sdk.pipelines.sources.spark.eventhub import SparkEventhubSource
from rtdip_sdk.pipelines.transformers.spark.binary_to_string import (
    BinaryToStringTransformer,
)
from rtdip_sdk.pipelines.transformers.spark.honeywell_apm_to_pcdm import (
    HoneywellAPMJsonToPCDMTransformer,
)
from rtdip_sdk.pipelines.destinations.spark.pcdm_to_delta import (
    SparkPCDMToDeltaDestination,
)
from rtdip_sdk.pipelines.utilities import SparkSessionUtility
import json

def pipeline():
    spark = SparkSessionUtility(config={}).execute()
    eventhub_source_configuration = {
        "eventhubs.connectionString": "{Endpoint=sb://mynamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=XXXXXXXXXXXX}",
        "eventhubs.consumerGroup": "$Default",
        "eventhubs.startingPosition": json.dumps(
            {"offset": "0", "seqNo": -1, "enqueuedTime": None, "isInclusive": True}
        ),
    }
    hw_source_df = SparkEventhubSource(spark, eventhub_source_configuration).read_batch()
    hw_raw_df = BinaryToStringTransformer(hw_source_df, "body", "body").transform()
    pcdm_df = HoneywellAPMJsonToPCDMTransformer(hw_raw_df, "body").transform()

    SparkPCDMToDeltaDestination(
        spark=spark,
        data=pcdm_df,
        options={},
        destination_float="{/path/to/table}",
        mode="overwrite",
        merge=False,
    ).write_batch()

if __name__ == "__main__":
    pipeline()

