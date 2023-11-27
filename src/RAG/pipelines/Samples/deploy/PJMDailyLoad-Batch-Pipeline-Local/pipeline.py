import sys, os

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from rtdip_sdk.pipelines.sources import PJMDailyLoadISOSource
from rtdip_sdk.pipelines.transformers import PJMToMDMTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaDestination
from pyspark.sql import SparkSession

def pipeline():
    spark = SparkSession.builder.config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0")\
                                .config("spark.sql.extensions","io.delta.sql.DeltaSparkSessionExtension")\
                                .config("spark.sql.catalog.spark_catalog","org.apache.spark.sql.delta.catalog.DeltaCatalog").getOrCreate()

    source_df = PJMDailyLoadISOSource(
        spark = spark,
        options = {
            "api_key": "{api_key}", 
            "load_type": "actual"
        }
    ).read_batch()

    transform_value_df = PJMToMDMTransformer(
        spark=spark,
        data=source_df,
        output_type= "usage"
    ).transform()

    transform_meta_df = PJMToMDMTransformer(
        spark=spark,
        data=source_df,
        output_type= "meta"
    ).transform()

    SparkDeltaDestination(
        data=transform_value_df,
        options={
            "partitionBy":"timestamp"
        },   
        destination="pjm_usage_data"
    ).write_batch()    

    SparkDeltaDestination(
        data=transform_meta_df,
        options={
            "partitionBy":"timestamp"
        },   
        destination="pjm_meta_data"
    ).write_batch() 

if __name__ == "__main__":
    pipeline()