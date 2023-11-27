from rtdip_sdk.pipelines.sources.python.delta import PythonDeltaSource
from rtdip_sdk.pipelines.destinations.python.delta import PythonDeltaDestination

source = PythonDeltaSource("{/path/to/source/table}").read_batch()

destination = PythonDeltaDestination(source, "{/path/to/destination/table}", mode="append").write_batch()
