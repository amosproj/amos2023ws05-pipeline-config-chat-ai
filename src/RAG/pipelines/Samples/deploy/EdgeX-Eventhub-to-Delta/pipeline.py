from rtdip_sdk.pipelines.sources.spark.eventhub import SparkEventhubSource
from rtdip_sdk.pipelines.transformers.spark.binary_to_string import (
    BinaryToStringTransformer,
)
from rtdip_sdk.pipelines.destinations.spark.delta import SparkDeltaDestination
from rtdip_sdk.pipelines.transformers.spark.edgex_opcua_json_to_pcdm import (
    EdgeXOPCUAJsonToPCDMTransformer,
)
from rtdip_sdk.pipelines.utilities import SparkSessionUtility
import json


def pipeline():

    spark = SparkSessionUtility(config={}).execute()

    ehConf = {
        "eventhubs.connectionString": "{EventhubConnectionString}",
        "eventhubs.consumerGroup": "{EventhubConsumerGroup}",
        "eventhubs.startingPosition": json.dumps(
            {"offset": "0", "seqNo": -1, "enqueuedTime": None, "isInclusive": True}
        ),
    }

    source = SparkEventhubSource(spark, ehConf).read_batch()
    string_data = BinaryToStringTransformer(source, "body", "body").transform()
    PCDM_data = EdgeXOPCUAJsonToPCDMTransformer(string_data, "body").transform()
    SparkDeltaDestination(
        data=PCDM_data, options={}, destination="{path/to/table}"
    ).write_batch()


if __name__ == "__main__":
    pipeline()
