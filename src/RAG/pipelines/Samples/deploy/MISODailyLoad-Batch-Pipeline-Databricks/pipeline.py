from rtdip_sdk.pipelines.sources import MISODailyLoadISOSource
from rtdip_sdk.pipelines.transformers import MISOToMDMTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

def pipeline():   
    source_df = MISODailyLoadISOSource(
        spark = spark,
        options = {
        "load_type": "actual",
        "date": "20230520",
        }
    ).read_batch()

    transform_value_df = MISOToMDMTransformer(
        spark=spark,
        data=source_df,
        output_type= "usage"
    ).transform()

    transform_meta_df = MISOToMDMTransformer(
        spark=spark,
        data=source_df,
        output_type= "meta"
    ).transform()

    SparkDeltaDestination(
        data=transform_value_df,
        options={
            "partitionBy":"timestamp"
        },   
        destination="miso_usage_data" 
    ).write_batch()    

    SparkDeltaDestination(
        data=transform_meta_df,
        options={
            "partitionBy":"timestamp"
        },   
        destination="miso_meta_data",
        mode="overwrite"
    ).write_batch() 

if __name__ == "__main__":
    pipeline()