from rtdip_sdk.pipelines.sources.spark.eventhub import SparkEventhubSource
from rtdip_sdk.pipelines.transformers.spark.binary_to_string import (
    BinaryToStringTransformer,
)
from rtdip_sdk.pipelines.transformers.spark.fledge_opcua_json_to_pcdm import (
    FledgeOPCUAJsonToPCDMTransformer,
)
from rtdip_sdk.pipelines.transformers.spark.pcdm_to_honeywell_apm import (
    PCDMToHoneywellAPMTransformer,
)
from rtdip_sdk.pipelines.destinations.spark.eventhub import SparkEventhubDestination
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

    source_df = SparkEventhubSource(spark, eventhub_source_configuration).read_batch()
    fledge_df = BinaryToStringTransformer(source_df, "body", "body").transform()
    pcdm_df = FledgeOPCUAJsonToPCDMTransformer(fledge_df, "body").transform()
    hw_apm_df = PCDMToHoneywellAPMTransformer(
        pcdm_df, history_samples_per_message=5
    ).transform()
    eventhub_destination_configuration = {
        "eventhubs.connectionString": "{Endpoint=sb://mynamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=XXXXXXXXXXXX}",
    }
    SparkEventhubDestination(
        spark, data=hw_apm_df, options=eventhub_destination_configuration
    ).write_batch()


if __name__ == "__main__":
    pipeline()
