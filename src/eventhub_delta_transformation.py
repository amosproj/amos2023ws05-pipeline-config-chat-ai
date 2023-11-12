from rtdip_sdk.pipelines.destinations import SparkDeltaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility
from rtdip_sdk.pipelines.sources import SparkEventhubSource
from rtdip_sdk.pipelines.transformers import BinaryToStringTransformer, EdgeXOPCUAJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility
import json


spark = SparkSessionUtility(config={}).execute()

ehConf = {
    "eventhubs.connectionString": "Endpoint=sb://iothub-ns-iotamosdem-25345447-44b7687241.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=us1Gf13qVMDD5V+ojCUWJcBO5NMxJ3FVqAIoTCcwxRo=;EntityPath=iotamosdemo",
    "eventhubs.consumerGroup": "amos-cg-obeidah",
    "eventhubs.startingPosition": json.dumps(
        {"offset": "0", "seqNo": -1, "enqueuedTime": None, "isInclusive": True}
    ),
}

source = SparkEventhubSource(spark, ehConf).read_batch()

string_data = BinaryToStringTransformer(source, "body", "body").transform()

edge_data = EdgeXOPCUAJsonToPCDMTransformer(string_data, "body").transform()

edge_data.show()

SparkDeltaDestination(
    data=edge_data, 
    options={
        "spark.sql.warehouse.dir": "/Users/obi/Desktop/AMOS/spark-warehouse",
    }, 
    destination="test_spark_delta_write_batch"
).write_batch()
