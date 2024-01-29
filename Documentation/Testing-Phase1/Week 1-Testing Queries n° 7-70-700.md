# Testing Queries n° 7-70-700

Créé par: Nahrain Gtari
Heure de création: 19. Dezember 2023 14:08

Q7: I would like to use RTDIP components to read from PythonDeltaSource , transform using BaseRawToMDMTransformer then write to SparkKafkaEventhubDestination

```python
from rtdip.pipeline import Pipeline
from rtdip.components.sources.python.delta import PythonDeltaSource
from rtdip.components.transformers.python.base_raw_to_mdm import BaseRawToMDMTransformer
from rtdip.components.destinations.spark.kafka_eventhub import SparkKafkaEventhubDestination

# Create the pipeline
pipeline = Pipeline()

# Add the source component
source = PythonDeltaSource(
    table_name="your_delta_table_name"
)
pipeline.add_component(source)

# Add the transformer component
transformer = BaseRawToMDMTransformer()
pipeline.add_component(transformer)

# Add the destination component
destination = SparkKafkaEventhubDestination(
    broker_list="your_kafka_broker_list",
    topic="your_kafka_topic"
)
pipeline.add_component(destination)

# Connect the components
pipeline.connect(source, transformer)
pipeline.connect(transformer, destination)

# Run the pipeline
pipeline.run()
```

Q70: I would like to use RTDIP components to read from PythonDeltaSource , transform using PandasToPySparkTransformer then write to SparkDeltaMergeDestination

```python
from rtdip_sdk.pipelines.sources import PythonDeltaSource
from rtdip_sdk.pipelines.transformers import PandasToPySparkTransformer
from rtdip_sdk.pipelines.destinations import SparkDeltaMergeDestination

def pipeline():
    source_df = PythonDeltaSource(
        delta_table_path="path/to/delta/table"
    ).read_batch()

    transformed_df = PandasToPySparkTransformer(
        data=source_df
    ).transform()

    SparkDeltaMergeDestination(
        data=transformed_df,
        options={
            "mergeCondition": "merge_condition",
            "mergeKey": "merge_key",
            "updateColumns": ["col1", "col2"],
            "deleteColumns": ["col3"]
        },
        destination="path/to/merge/destination"
    ).write_batch()

if __name__ == "__main__":
    pipeline()
```

Q700: I would like to use RTDIP components to read from SparkDeltaSource , transform using SEMJsonToPCDMTransformer then write to SparkKafkaEventhubDestination

```python
from rtdip_sdk.pipelines.sources.spark.delta import SparkDeltaSource
from rtdip_sdk.pipelines.transformers.spark.sem_json_to_pcdm import SEMJsonToPCDMTransformer
from rtdip_sdk.pipelines.destinations.spark.kafka_eventhub import SparkKafkaEventhubDestination
from rtdip_sdk.pipelines.utilities import SparkSessionUtility
import json

def pipeline():
    spark = SparkSessionUtility(config={}).execute()

    delta_source_configuration = {
        "delta.path": "/path/to/delta_table"
    }

    source_df = SparkDeltaSource(spark, delta_source_configuration).read_batch()
    pcdm_df = SEMJsonToPCDMTransformer(source_df, "body").transform()

    kafka_eventhub_destination_configuration = {
        "kafka.bootstrap.servers": "your.kafka.bootstrap.servers",
        "eventhubs.connectionString": "{EventhubConnectionString}"
    }

    SparkKafkaEventhubDestination(
        spark, data=pcdm_df, options=kafka_eventhub_destination_configuration
    ).write_batch()

if __name__ == "__main__":
    pipeline()
```