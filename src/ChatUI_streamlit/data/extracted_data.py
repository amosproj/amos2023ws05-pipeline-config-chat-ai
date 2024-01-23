The type of the system.
    Unpivot the data. Convert column values into rows.

    Args:
        df: Data to be unpivot.
        id_vars: Columns to keep after unpivot.
        value_vars: Columns to be converted into rows.
        var_name: New column name to store previous column names.
        value_name: New column name to store values of unpivoted columns.

    Returns: Data after unpivot process.

    
    Deploys an RTDIP Pipeline to Databricks Workflows leveraging the Databricks [SDK.](https://docs.databricks.com/dev-tools/sdk-python.html)

    Deploying an RTDIP Pipeline to Databricks requires only a few additional pieces of information to ensure the RTDIP Pipeline Job can be run in Databricks. This information includes:

    - **Cluster**: This can be defined a the Job or Task level and includes the size of the cluster to be used for the job
    - **Task**: The cluster to be used to execute the task, as well as any task scheduling information, if required.

    All options available in the [Databricks Jobs REST API v2.1](https://docs.databricks.com/dev-tools/api/latest/jobs.html) can be configured in the Databricks classes that have been defined in `rtdip_sdk.pipelines.deploy.models.databricks`, enabling full control of the configuration of the Databricks Workflow :

    - `CreateJob`
    - `Task`

    RTDIP Pipeline Components provide Databricks with all the required Python packages and JARs to execute each component and these will be setup on the Workflow automatically during the Databricks Workflow creation.

    Example:
        This example assumes that a PipelineJob has already been defined by a variable called `pipeline_job`

        ```python
        from rtdip_sdk.pipelines.deploy import DatabricksSDKDeploy, CreateJob, JobCluster, ClusterSpec, Task, NotebookTask, ComputeSpecKind, AutoScale, RuntimeEngine, DataSecurityMode

        cluster_list = []
        cluster_list.append(JobCluster(
            job_cluster_key="test_cluster",
            new_cluster=ClusterSpec(
                node_type_id="Standard_E4ds_v5",
                autoscale=AutoScale(min_workers=1, max_workers=3),
                spark_version="13.2.x-scala2.12",
                data_security_mode=DataSecurityMode.SINGLE_USER,
                runtime_engine=RuntimeEngine.PHOTON
            )
        ))

        task_list = []
        task_list.append(Task(
            task_key="test_task",
            job_cluster_key="test_cluster",
            notebook_task=NotebookTask(
                notebook_path="/path/to/pipeline/rtdip_pipeline.py"
            )
        ))

        job = CreateJob(
            name="test_job_rtdip",
            job_clusters=cluster_list,
            tasks=task_list
        )

        databricks_job = DatabricksSDKDeploy(databricks_job=job, host="https://test.databricks.net", token="test_token")

        # Execute the deploy method to create a Workflow in the specified Databricks Environment
        deploy_result = databricks_job.deploy()

        # If the job should be executed immediately, execute the `launch` method
        launch_result = databricks_job.launch()
        ```

    Parameters:
        databricks_job (DatabricksJob): Contains Databricks specific information required for deploying the RTDIP Pipeline Job to Databricks, such as cluster and workflow scheduling information. This can be any field in the [Databricks Jobs REST API v2.1](https://docs.databricks.com/dev-tools/api/latest/jobs.html)
        host (str): Databricks URL
        token (str): Token for authenticating with Databricks such as a Databricks PAT Token or Azure AD Token
        workspace_directory (str, optional): Determines the folder location in the Databricks Workspace. Defaults to /rtdip
    
        Deploys an RTDIP Pipeline Job to Databricks Workflows. The deployment is managed by the Job Name and therefore will overwrite any existing workflow in Databricks with the same name.
        
        Launches an RTDIP Pipeline Job in Databricks Workflows. This will perform the equivalent of a `Run Now` in Databricks Workflows
        
    The Python Delta Destination is used to write data to a Delta table from a Polars LazyFrame.

     Example
    --------
    === "Azure"

        ```python
        from rtdip_sdk.pipelines.destinations import PythonDeltaDestination

        path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}

        python_delta_destination = PythonDeltaDestination(
            data=LazyFrame
            path=path,
            storage_options={
                "azure_storage_account_name": "{AZURE-STORAGE-ACCOUNT-NAME}",
                "azure_storage_account_key": "{AZURE-STORAGE-ACCOUNT-KEY}"
            },
            mode=:error",
            overwrite_schema=False,
            delta_write_options=None
        )

        python_delta_destination.read_batch()

        ```
    === "AWS"

        ```python
        from rtdip_sdk.pipelines.destinations import PythonDeltaDestination

        path = "https://s3.{REGION-CODE}.amazonaws.com/{BUCKET-NAME}/{KEY-NAME}"

        python_delta_destination = PythonDeltaDestination(
            data=LazyFrame
            path=path,
            options={
                "aws_access_key_id": "{AWS-ACCESS-KEY-ID}",
                "aws_secret_access_key": "{AWS-SECRET-ACCESS-KEY}"
            },
            mode=:error",
            overwrite_schema=False,
            delta_write_options=None
        )

        python_delta_destination.read_batch()
        ```

    Parameters:
        data (LazyFrame): Polars LazyFrame to be written to Delta
        path (str): Path to Delta table to be written to; either local or [remote](https://delta-io.github.io/delta-rs/python/usage.html#loading-a-delta-table){ target="_blank" }. **Locally** if the Table does't exist one will be created, but to write to AWS or Azure, you must have an existing Delta Table
        options (Optional dict): Used if writing to a remote location. For AWS use format {"aws_access_key_id": "<>", "aws_secret_access_key": "<>"}. For Azure use format {"azure_storage_account_name": "storageaccountname", "azure_storage_access_key": "<>"}
        mode (Literal['error', 'append', 'overwrite', 'ignore']): Defaults to error if table exists, 'ignore' won't write anything if table exists
        overwrite_schema (bool): If True will allow for the table schema to be overwritten
        delta_write_options (dict): Options when writing to a Delta table. See [here](https://delta-io.github.io/delta-rs/python/api_reference.html#writing-deltatables){ target="_blank" } for all options
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
        Writes batch data to Delta without using Spark.
        
        Raises:
            NotImplementedError: Writing to a Delta table using Python is only possible for batch writes. To perform a streaming read, use the write_stream method of the SparkDeltaDestination component.
        
    The EVM Contract Destination is used to write to a smart contract blockchain.

    Examples
    --------
    ```python
    from rtdip_sdk.pipelines.destinations import EVMContractDestination

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

    evm_contract_destination.write_batch()
    ```

    Parameters:
        url (str): Blockchain network URL e.g. 'https://polygon-mumbai.g.alchemy.com/v2/⟨API_KEY⟩'
        account (str): Address of the sender that will be signing the transaction.
        private_key (str): Private key for your blockchain account.
        abi (json str): Smart contract's ABI.
        contract (str): Address of the smart contract.
        function_name (str): Smart contract method to call on.
        function_params (tuple): Parameters of given function.
        transaction (dict): A dictionary containing a set of instructions to interact with a smart contract deployed on the blockchain (See common parameters in Attributes table below).

    Attributes:
        data (hexadecimal str): Additional information store in the transaction.
        from (hexadecimal str): Address of sender for a transaction.
        gas (int): Amount of gas units to perform a transaction.
        gasPrice (int Wei): Price to pay for each unit of gas. Integers are specified in Wei, web3's to_wei function can be used to specify the amount in a different currency.
        nonce (int): The number of transactions sent from a given address.
        to (hexadecimal str): Address of recipient for a transaction.
        value (int Wei): Value being transferred in a transaction. Integers are specified in Wei, web3's to_wei function can be used to specify the amount in a different currency.
    
        Writes to a smart contract deployed in a blockchain and returns the transaction hash.

        Example:
        ```
        from web3 import Web3

        web3 = Web3(Web3.HTTPProvider("https://polygon-mumbai.g.alchemy.com/v2/<API_KEY>"))

        x = EVMContractDestination(
                            url="https://polygon-mumbai.g.alchemy.com/v2/<API_KEY>",
                            account='<ACCOUNT>',
                            private_key='<PRIVATE_KEY>',
                            contract='<CONTRACT>',
                            function_name='transferFrom',
                            function_params=('<FROM_ACCOUNT>', '<TO_ACCOUNT>', 0),
                            abi = 'ABI',
                            transaction={
                                'gas': 100000,
                                'gasPrice': 1000000000 # or web3.to_wei('1', 'gwei')
                                },
                            )

        print(x.write_batch())
        ```
        
        Raises:
            NotImplementedError: Write stream is not supported.
        
    This Spark Destination class is used to write batch or streaming data to an Eventhub using the Kafka protocol. This enables Eventhubs to be used as a destination in applications like Delta Live Tables or Databricks Serverless Jobs as the Spark Eventhubs JAR is not supported in these scenarios.

    Default settings will be specified if not provided in the `options` parameter:

    - `kafka.sasl.mechanism` will be set to `PLAIN`
    - `kafka.security.protocol` will be set to `SASL_SSL`
    - `kafka.request.timeout.ms` will be set to `60000`
    - `kafka.session.timeout.ms` will be set to `60000`

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.destinations import SparkKafkaEventhubDestination
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}

    eventhub_destination = SparkKafkaEventhubDestination(
        spark=spark,
        data=df,
        options={
            "kafka.bootstrap.servers": "host1:port1,host2:port2"
        },
        consumer_group="{YOUR-EVENTHUB-CONSUMER-GROUP}",
        trigger="10 seconds",
        query_name="KafkaEventhubDestination",
        query_wait_interval=None
    )

    eventhub_destination.write_stream()

    OR

    eventhub_destination.write_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        data (DataFrame): Any columns not listed in the required schema [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html#writing-data-to-kafka){ target="_blank" } will be merged into a single column named "value", or ignored if "value" is an existing column
        connection_string (str): Eventhubs connection string is required to connect to the Eventhubs service. This must include the Eventhub name as the `EntityPath` parameter. Example `"Endpoint=sb://test.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=test_key;EntityPath=test_eventhub"`
        options (dict): A dictionary of Kafka configurations (See Attributes tables below)
        consumer_group (str): The Eventhub consumer group to use for the connection
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (optional str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    The following are commonly used parameters that may be included in the options dict. kafka.bootstrap.servers is the only required config. A full list of configs can be found [here](https://kafka.apache.org/documentation/#producerconfigs){ target="_blank" }

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port):  The Kafka "bootstrap.servers" configuration. (Streaming and Batch)
        topic (string): Required if there is no existing topic column in your DataFrame. Sets the topic that all rows will be written to in Kafka. (Streaming and Batch)
        includeHeaders (bool): Determines whether to include the Kafka headers in the row; defaults to False. (Streaming and Batch)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from Kafka.
        
        Reads streaming data from Kafka.
        
    This Spark destination class is used to write batch or streaming data to Eventhubs. Eventhub configurations need to be specified as options in a dictionary.
    Additionally, there are more optional configurations which can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
    If using startingPosition or endingPosition make sure to check out **Event Position** section for more details and examples.

    Examples
    --------
    ```python
    #Eventhub Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkEventhubDestination
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}

    eventhub_destination = SparkEventhubDestination(
        spark=spark,
        data=df,
        options={
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-EVENTHUB-CONSUMER-GROUP}",
            "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
        },
        trigger="10 seconds",
        query_name="EventhubDestination",
        query_wait_interval=None
    )

    eventhub_destination.write_stream()
    ```
    ```python
    #Eventhub Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkEventhubDestination
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}


    eventhub_destination = SparkEventhubDestination(
        spark=spark,
        data=df,
        options={
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-EVENTHUB-CONSUMER-GROUP}"
        },
        trigger="10 seconds",
        query_name="EventhubDestination",
        query_wait_interval=None
    )

    eventhub_destination.write_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        data (DataFrame): Dataframe to be written to Eventhub
        options (dict): A dictionary of Eventhub configurations (See Attributes table below). All Configuration options for Eventhubs can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
        eventhubs.connectionString (str):  Eventhubs connection string is required to connect to the Eventhubs service. (Streaming and Batch)
        eventhubs.consumerGroup (str): A consumer group is a view of an entire eventhub. Consumer groups enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their own offsets. (Streaming and Batch)
        eventhubs.startingPosition (JSON str): The starting position for your Structured Streaming job. If a specific EventPosition is not set for a partition using startingPositions, then we use the EventPosition set in startingPosition. If nothing is set in either option, we will begin consuming from the end of the partition. (Streaming and Batch)
        eventhubs.endingPosition: (JSON str): The ending position of a batch query. This works the same as startingPosition. (Batch)
        maxEventsPerTrigger (long): Rate limit on maximum number of events processed per trigger interval. The specified total number of events will be proportionally split across partitions of different volume. (Stream)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Writes batch data to Eventhubs.
        
        Writes steaming data to Eventhubs.
        
    The Process Control Data Model Latest Values written to Delta.

    Example
    --------
    ```python
    #PCDM Latest To Delta Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMLatestToDeltaDestination

    pcdm_latest_to_delta_destination = SparkPCDMLatestToDeltaDestination(
        data=df,
        options={
            "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
        },
        destination="{DELTA_TABLE_PATH}",
        mode="append",
        trigger="10 seconds",
        query_name="PCDMLatestToDeltaDestination",
        query_wait_interval=None
    )

    pcdm_latest_to_delta_destination.write_stream()
    ```
    ```python
    #PCDM Latest To Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMLatestToDeltaDestination

    pcdm_latest_to_delta_destination = SparkPCDMLatestToDeltaDestination(
        data=df,
        options={
            "maxRecordsPerFile", "10000"
        },
        destination="{DELTA_TABLE_PATH}",
        mode="overwrite",
        trigger="10 seconds",
        query_name="PCDMLatestToDeltaDestination",
        query_wait_interval=None
    )

    pcdm_latest_to_delta_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        destination (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store the latest values
        mode (str): Method of writing to Delta Table - append/overwrite (batch), append/complete (stream)
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Writes Process Control Data Model data to Delta
        
        Writes streaming Process Control Data Model data to Delta using foreachBatch
        
    This Kinesis destination class is used to write batch or streaming data to Kinesis. Kinesis configurations need to be specified as options in a dictionary.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.destinations import SparkKinesisDestination

    kinesis_destination = SparkKinesisDestination(
        data=df,
        options={
            "endpointUrl": "https://kinesis.{REGION}.amazonaws.com",
            "awsAccessKey": "{YOUR-AWS-ACCESS-KEY}",
            "awsSecretKey": "{YOUR-AWS-SECRET-KEY}",
            "streamName": "{YOUR-STREAM-NAME}"
        },
        mode="update",
        trigger="10 seconds",
        query_name="KinesisDestination",
        query_wait_interval=None
    )

    kinesis_destination.write_stream()

    OR

    kinesis_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be written to Delta
        options (dict): A dictionary of Kinesis configurations (See Attributes table below). All Configuration options for Kinesis can be found [here.](https://github.com/qubole/kinesis-sql#kinesis-sink-configuration){ target="_blank" }
        mode (str): Method of writing to Kinesis - append, complete, update
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        endpointUrl (str): Endpoint of the kinesis stream.
        awsAccessKey (str): AWS access key.
        awsSecretKey (str): AWS secret access key corresponding to the access key.
        streamName (List[str]): Name of the streams in Kinesis to write to.
    
        Attributes:
            SystemType (Environment): Requires PYSPARK_DATABRICKS
        
        Writes batch data to Kinesis.
        
        Writes steaming data to Kinesis.
        
    The Process Control Data Model written to Delta.

    Example
    --------
    ```python
    #PCDM Latest To Delta Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMToDeltaDestination

    pcdm_to_delta_destination = SparkPCDMToDeltaDestination(
        data=df,
        options={
            "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
        },
        destination_float="{DELTA_TABLE_PATH_FLOAT}",
        destination_string="{DELTA_TABLE_PATH_STRING}",
        destination_integer="{DELTA_TABLE_PATH_INTEGER}",
        mode="append",
        trigger="10 seconds",
        query_name="PCDMToDeltaDestination",
        query_wait_interval=None,
        merge=True,
        try_broadcast_join=False,
        remove_nanoseconds=False,
        remove_duplicates-True
    )

    pcdm_to_delta_destination.write_stream()
    ```
    ```python
    #PCDM Latest To Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkPCDMToDeltaDestination

    pcdm_to_delta_destination = SparkPCDMToDeltaDestination(
        data=df,
        options={
            "maxRecordsPerFile", "10000"
        },
        destination_float="{DELTA_TABLE_PATH_FLOAT}",
        destination_string="{DELTA_TABLE_PATH_STRING}",
        destination_integer="{DELTA_TABLE_PATH_INTEGER}",
        mode="overwrite",
        trigger="10 seconds",
        query_name="PCDMToDeltaDestination",
        query_wait_interval=None,
        merge=True,
        try_broadcast_join=False,
        remove_nanoseconds=False,
        remove_duplicates-True
    )

    pcdm_to_delta_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        destination_float (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store float values.
        destination_string (Optional str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store string values.
        destination_integer (Optional str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table to store integer values
        mode (str): Method of writing to Delta Table - append/overwrite (batch), append/complete (stream)
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None
        merge (bool): Use Delta Merge to perform inserts, updates and deletes
        try_broadcast_join (bool): Attempts to perform a broadcast join in the merge which can leverage data skipping using partition pruning and file pruning automatically. Can fail if dataframe being merged is large and therefore more suitable for streaming merges than batch merges
        remove_nanoseconds (bool): Removes nanoseconds from the EventTime column and replaces with zeros
        remove_duplicates (bool: Removes duplicates before writing the data

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Writes Process Control Data Model data to Delta
        
        Writes streaming Process Control Data Model data to Delta using foreachBatch
        
    The Spark Delta Merge Destination is used to merge data into a Delta table. Refer to this [documentation](https://docs.delta.io/latest/delta-update.html#upsert-into-a-table-using-merge&language-python) for more information about Delta Merge.

    Examples
    --------
    ```python
    #Delta Merge Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaMergeDestination

    delta_merge_destination = SparkDeltaMergeDestination(
        data=df,
        destination="DELTA-TABLE-PATH",
        options={
            "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
        },
        merge_condition="`source.id = target.id`"
        when_matched_update_list=None
        when_matched_delete_list=None
        when_not_matched_insert_list=None
        when_not_matched_by_source_update_list=None
        when_not_matched_by_source_delete_list=None
        try_broadcast_join=False
        trigger="10 seconds",
        query_name="DeltaDestination"
        query_wait_interval=None
    )

    delta_merge_destination.write_stream()
    ```
    ```python
    #Delta Merge Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaMergeDestination

    delta_merge_destination = SparkDeltaMergeDestination(
        data=df,
        destination="DELTA-TABLE-PATH",
        options={},
        merge_condition="`source.id = target.id`",
        when_matched_update_list=None,
        when_matched_delete_list=None,
        when_not_matched_insert_list=None,
        when_not_matched_by_source_update_list=None,
        when_not_matched_by_source_delete_list=None,
        try_broadcast_join=False,
        trigger="10 seconds",
        query_name="DeltaDestination"
        query_wait_interval=None
    )

    delta_merge_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        destination (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        merge_condition (str): Condition for matching records between dataframe and delta table. Reference Dataframe columns as `source` and Delta Table columns as `target`. For example `source.id = target.id`.
        when_matched_update_list (optional list[DeltaMergeConditionValues]): Conditions(optional) and values to be used when updating rows that match the `merge_condition`. Specify `*` for Values if all columns from Dataframe should be inserted.
        when_matched_delete_list (optional list[DeltaMergeCondition]): Conditions(optional) to be used when deleting rows that match the `merge_condition`.
        when_not_matched_insert_list (optional list[DeltaMergeConditionValues]): Conditions(optional) and values to be used when inserting rows that do not match the `merge_condition`. Specify `*` for Values if all columns from Dataframe should be inserted.
        when_not_matched_by_source_update_list (optional list[DeltaMergeConditionValues]): Conditions(optional) and values to be used when updating rows that do not match the `merge_condition`.
        when_not_matched_by_source_delete_list (optional list[DeltaMergeCondition]): Conditions(optional) to be used when deleting rows that do not match the `merge_condition`.
        try_broadcast_join (optional bool): Attempts to perform a broadcast join in the merge which can leverage data skipping using partition pruning and file pruning automatically. Can fail if dataframe being merged is large and therefore more suitable for streaming merges than batch merges
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (optional str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Merges batch data into a Delta Table.
        
        Merges streaming data to Delta using foreachBatch
        
    This Spark destination class is used to write batch or streaming data from Kafka. Required and optional configurations can be found in the Attributes tables below.

    Additionally, there are more optional configurations which can be found [here.](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }

    For compatibility between Spark and Kafka, the columns in the input dataframe are concatenated into one 'value' column of JSON string.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.destinations import SparkKafkaDestination

    kafka_destination = SparkKafkaDestination(
        data=df,
        options={
            "kafka.bootstrap.servers": "host1:port1,host2:port2"
        },
        trigger="10 seconds",
        query_name="KafkaDestination",
        query_wait_interval=None
    )

    kafka_destination.write_stream()

    OR

    kafka_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be written to Kafka
        options (dict): A dictionary of Kafka configurations (See Attributes tables below). For more information on configuration options see [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    The following options must be set for the Kafka destination for both batch and streaming queries.

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port): The Kafka "bootstrap.servers" configuration. (Streaming and Batch)

    The following configurations are optional:

    Attributes:
        topic (str):Sets the topic that all rows will be written to in Kafka. This option overrides any topic column that may exist in the data. (Streaming and Batch)
        includeHeaders (bool): Whether to include the Kafka headers in the row. (Streaming and Batch)

    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Writes batch data to Kafka.
        
        Writes steaming data to Kafka.
        
    The Spark Delta Destination is used to write data to a Delta table.

    Examples
    --------
    ```python
    #Delta Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

    delta_destination = SparkDeltaDestination(
        data=df,
        options={
            "checkpointLocation": "/{CHECKPOINT-LOCATION}/"
        },
        destination="DELTA-TABLE-PATH",
        mode="append",
        trigger="10 seconds",
        query_name="DeltaDestination",
        query_wait_interval=None
    )

    delta_destination.write_stream()
    ```
    ```python
    #Delta Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkDeltaDestination

    delta_destination = SparkDeltaDestination(
        data=df,
        options={
            "overwriteSchema": True
        },
        destination="DELTA-TABLE-PATH",
        mode="append",
        trigger="10 seconds",
        query_name="DeltaDestination",
        query_wait_interval=None
    )

    delta_destination.write_batch()
    ```

    Parameters:
        data (DataFrame): Dataframe to be written to Delta
        options (dict): Options that can be specified for a Delta Table write operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#write-to-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-sink){ target="_blank" }.
        destination (str): Either the name of the Hive Metastore or Unity Catalog Delta Table **or** the path to the Delta table
        mode (optional str): Method of writing to Delta Table - append/overwrite (batch), append/update/complete (stream). Default is append
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (optional str): Unique name for the query in associated SparkSession. (stream) Default is DeltaDestination
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
        txnAppId (str): A unique string that you can pass on each DataFrame write. (Batch & Streaming)
        txnVersion (str): A monotonically increasing number that acts as transaction version. (Batch & Streaming)
        maxRecordsPerFile (int str): Specify the maximum number of records to write to a single file for a Delta Lake table. (Batch)
        replaceWhere (str): Condition(s) for overwriting. (Batch)
        partitionOverwriteMode (str): When set to dynamic, overwrites all existing data in each logical partition for which the write will commit new data. Default is static. (Batch)
        overwriteSchema (bool str): If True, overwrites the schema as well as the table data. (Batch)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Writes batch data to Delta. Most of the options provided by the Apache Spark DataFrame write API are supported for performing batch writes on tables.
        
        Writes streaming data to Delta. Exactly-once processing is guaranteed
        
    The Spark Rest API Destination is used to write data to a Rest API.

    The payload sent to the API is constructed by converting each row in the DataFrame to Json.

    !!! Note
        While it is possible to use the `write_batch` method, it is easy to overwhlem a Rest API with large volumes of data.
        Consider reducing data volumes when writing to a Rest API in Batch mode to prevent API errors including throtting.

    Example
    --------
    ```python
    #Rest API Destination for Streaming Queries

    from rtdip_sdk.pipelines.destinations import SparkRestAPIDestination

    rest_api_destination = SparkRestAPIDestination(
        data=df,
        options={
            "checkpointLocation": "{/CHECKPOINT-LOCATION/}"
        },
        url="{REST-API-URL}",
        headers = {
            'Authorization': 'Bearer {}'.format("{TOKEN}")
        },
        batch_size=100,
        method="POST",
        parallelism=8,
        trigger="1 minute",
        query_name="DeltaRestAPIDestination",
        query_wait_interval=None
    )

    rest_api_destination.write_stream()
    ```
    ```python
    #Rest API Destination for Batch Queries

    from rtdip_sdk.pipelines.destinations import SparkRestAPIDestination

    rest_api_destination = SparkRestAPIDestination(
        data=df,
        options={},
        url="{REST-API-URL}",
        headers = {
            'Authorization': 'Bearer {}'.format("{TOKEN}")
        },
        batch_size=10,
        method="POST",
        parallelism=4,
        trigger="1 minute",
        query_name="DeltaRestAPIDestination",
        query_wait_interval=None
    )

    rest_api_destination.write_stream()
    ```

    Parameters:
        data (DataFrame): Dataframe to be merged into a Delta Table
        options (dict): A dictionary of options for streaming writes
        url (str): The Rest API Url
        headers (dict): A dictionary of headers to be provided to the Rest API
        batch_size (int): The number of DataFrame rows to be used in each Rest API call
        method (str): The method to be used when calling the Rest API. Allowed values are POST, PATCH and PUT
        parallelism (int): The number of concurrent calls to be made to the Rest API
        trigger (optional str): Frequency of the write operation. Specify "availableNow" to execute a trigger once, otherwise specify a time period such as "30 seconds", "5 minutes". Set to "0 seconds" if you do not want to use a trigger. (stream) Default is 10 seconds
        query_name (str): Unique name for the query in associated SparkSession
        query_wait_interval (optional int): If set, waits for the streaming query to complete before returning. (stream) Default is None

    Attributes:
        checkpointLocation (str): Path to checkpoint files. (Streaming)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Writes batch data to a Rest API
        
        Writes streaming data to a Rest API
        
    Retrieves and creates/updates secrets in a Hashicorp Vault. For more information about Hashicorp Vaults, see [here.](https://developer.hashicorp.com/vault/docs/get-started/developer-qs)

    Example
    -------
    ```python
    # Retrieves Secrets from HashiCorp Vault

    from rtdip_sdk.pipelines.secrets import HashiCorpVaultSecrets

    get_hashicorp_secret = HashiCorpVaultSecrets(
        vault="http://127.0.0.1:8200",
        key="{KEY}",
        secret=None,
        credential="{CREDENTIAL}",
        kwargs=None
    )

    get_hashicorp_secret.get()

    ```
    ```python
    # Creates or Updates Secrets in Hashicorp Vault

    from rtdip_sdk.pipelines.secrets import HashiCorpVaultSecrets

    set_hashicorp_secret = AzureKeyVaultSecrets(
        vault="http://127.0.0.1:8200",
        key="{KEY}",
        secret="{SECRET-TO-BE-SET}",
        credential="{CREDENTIAL}",
        kwargs=None
    )

    set_hashicorp_secret.set()
    ```

    Parameters:
        vault (str): Hashicorp Vault URL
        key (str): Name/Key of the secret in the Hashicorp Vault
        secret (str): Secret or Password to be stored in the Hashicorp Vault
        credential (str): Token for authentication with the Hashicorp Vault
        kwargs (dict): List of additional parameters to be passed when creating a Hashicorp Vault Client. Please see [here](https://hvac.readthedocs.io/en/stable/overview.html#initialize-the-client) for more details on parameters that can be provided to the client
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
        Retrieves the secret from the Hashicorp Vault
        
        Creates or updates a secret in the Hashicorp Vault
        
    Retrieves secrets from Databricks Secret Scopes. For more information about Databricks Secret Scopes, see [here.](https://docs.databricks.com/security/secrets/secret-scopes.html)

    Example
    -------
    ```python
    # Reads Secrets from Databricks Secret Scopes

    from rtdip_sdk.pipelines.secrets import DatabricksSecrets
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    get_databricks_secret = DatabricksSecrets(
        spark=spark,
        vault="{NAME-OF-DATABRICKS-SECRET-SCOPE}"
        key="{KEY-NAME-OF-SECRET}",
    )

    get_databricks_secret.get()
    ```

    Parameters:
        spark: Spark Session required to read data from a Delta table
        vault: Name of the Databricks Secret Scope
        key: Name/Key of the secret in the Databricks Secret Scope
    
        Attributes:
            SystemType (Environment): Requires PYSPARK on Databricks
        
        Retrieves the secret from the Databricks Secret Scope
        
        Sets the secret in the Secret Scope
        Raises:
            NotImplementedError: Will be implemented at a later point in time
        
    Retrieves and creates/updates secrets in Azure Key Vault. For more information about Azure Key Vaults, see [here.](https://learn.microsoft.com/en-gb/azure/key-vault/general/overview)

    Example
    -------
    ```python
    # Retrieves Secrets from Azure Key Vault

    from rtdip_sdk.pipelines.secrets import AzureKeyVaultSecrets

    get_key_vault_secret = AzureKeyVaultSecrets(
        vault="https://{YOUR-KEY-VAULT}.azure.net/",
        key="{KEY}",
        secret=None,
        credential="{CREDENTIAL}",
        kwargs=None
    )

    get_key_vault_secret.get()

    ```
    ```python
    # Creates or Updates Secrets in Azure Key Vault

    from rtdip_sdk.pipelines.secrets import AzureKeyVaultSecrets

    set_key_vault_secret = AzureKeyVaultSecrets(
        vault="https://{YOUR-KEY-VAULT}.azure.net/",
        key="{KEY}",
        secret="{SECRET-TO-BE-SET}",
        credential="{CREDENTIAL}",
        kwargs=None
    )

    set_key_vault_secret.set()
    ```

    Parameters:
        vault (str): Azure Key Vault URL
        key (str): Key for the secret
        secret (str): Secret or Password to be set in the Azure Key Vault
        credential (str): Credential for authenticating with Azure Key Vault
        kwargs (dict): List of additional parameters to be passed when creating a Azure Key Vault Client. Please see [here](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/keyvault/azure-keyvault-secrets) for more details on parameters that can be provided to the client
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
        Retrieves the secret from the Azure Key Vault
        
        Creates or updates a secret in the Azure Key Vault
        
    Converts a json string into a Pipeline Job.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.secrets import PipelineJobFromJsonConverter

    convert_json_string_to_pipline_job = PipelineJobFromJsonConverter(
        pipeline_json = "{JSON-STRING}"
    )

    convert_json_string_to_pipline_job.convert()
    ```

    Parameters:
        pipeline_json (str): Json representing PipelineJob information, including tasks and related steps
    
        Converts a json string to a Pipeline Job
        
    Converts a Pipeline Job into a json string.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.secrets import PipelineJobToJsonConverter

    convert_pipeline_job_to_json_string = PipelineJobFromJsonConverter(
        pipeline_json = PipelineJob
    )

    convert_pipeline_job_to_json_string.convert()
    ```

    Parameters:
        pipeline_job (PipelineJob): A Pipeline Job consisting of tasks and steps
    
        Converts a Pipeline Job to a json string
        
    Gets the list of imported RTDIP components. Returns the libraries and settings of the components to be used in the pipeline.

    Call this component after all imports of the RTDIP components to ensure that the components can be determined.

    Parameters:
        module (optional str): Provide the module to use for imports of rtdip-sdk components. If not populated, it will use the calling module to check for imports
        spark_config (optional dict): Additional spark configuration to be applied to the spark session
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
    Assigns Azure AD Groups to ACLs on directories in an Azure Data Lake Store Gen 2 storage account.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import ADLSGen2DirectoryACLUtility

    adls_gen2_directory_acl_utility = ADLSGen2DirectoryACLUtility(
        storage_account="YOUR-STORAGAE-ACCOUNT-NAME",
        container="YOUR-ADLS_CONTAINER_NAME",
        credential="YOUR-TOKEN-CREDENTIAL",
        directory="DIRECTORY",
        group_object_id="GROUP-OBJECT",
        folder_permissions="r-x",
        parent_folder_permissions="r-x",
        root_folder_permissions="r-x",
        set_as_default_acl=True,
        create_directory_if_not_exists=True
    )

    result = adls_gen2_directory_acl_utility.execute()
    ```

    Parameters:
        storage_account (str): ADLS Gen 2 Storage Account Name
        container (str): ADLS Gen 2 Container Name
        credential (TokenCredential): Credentials to authenticate with ADLS Gen 2 Storage Account
        directory (str): Directory to be assign ACLS to in an ADLS Gen 2
        group_object_id (str): Azure AD Group Object ID to be assigned to Directory
        folder_permissions (optional, str): Folder Permissions to Assign to directory
        parent_folder_permissions (optional, str): Folder Permissions to Assign to parent directories. Parent Folder ACLs not set if None
        root_folder_permissions (optional, str): Folder Permissions to Assign to root directory. Root Folder ACL not set if None
        set_as_default_acl (bool, optional): Sets the ACL as the default ACL on the folder
        create_directory_if_not_exists (bool, optional): Creates the directory(and Parent Directories) if it does not exist
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
    Creates the required Azure Resources for the Databricks Autoloader Notification Mode.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import AzureAutoloaderResourcesUtility

    azure_autoloader_resources_utility = AzureAutoloaderResourcesUtility(
        subscription_id="YOUR-SUBSCRIPTION-ID",
        resource_group_name="YOUR-RESOURCE-GROUP",
        storage_account="YOUR-STORAGE-ACCOUNT-NAME",
        container="YOUR-CONTAINER-NAME",
        directory="DIRECTORY",
        credential="YOUR-CLIENT-ID",
        event_subscription_name="YOUR-EVENT-SUBSCRIPTION",
        queue_name="YOUR-QUEUE-NAME",
        system_topic_name=None
    )

    result = azure_autoloader_resources_utility.execute()
    ```

    Parameters:
        subscription_id (str): Azure Subscription ID
        resource_group_name (str): Resource Group Name of Subscription
        storage_account (str): Storage Account Name
        container (str): Container Name
        directory (str): Directory to be used for filtering messages in the Event Subscription. This will be equivalent to the Databricks Autoloader Path
        credential (TokenCredential): Credentials to authenticate with Storage Account
        event_subscription_name (str): Name of the Event Subscription
        queue_name (str): Name of the queue that will be used for the Endpoint of the Messages
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
    Copies an object from S3 to S3, from Local to S3 and S3 to local depending on the source and destination uri.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import S3CopyUtility

    s3_copy_utility = S3CopyUtility(
        source_uri="YOUR-SOURCE-URI",
        destination_uri="YOUR-DESTINATION-URI",
        source_version_id="YOUR-VERSION-ID",
        extra_args={},
        callback="YOUD-SID",
        source_client="PRINCIPAL",
        transfer_config=["ACTIONS"]
    )

    result = s3_bucket_policy_utility.execute()
    ```

    Parameters:
        source_uri (str): URI of the source object
        destination_uri (str): URI of the destination object
        source_version_id (optional str): Version ID of the source bucket
        extra_args (optional dict): Extra arguments that can be passed to the client operation. See [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.S3Transfer.ALLOWED_DOWNLOAD_ARGS){ target="_blank" } for a list of download arguments
        callback (optional function): Takes a UDF used for tracking the progress of the copy operation
        source_client (optional botocore or boto3 client): A different S3 client to use for the source bucket during the copy operation
        transfer_config (optional class): The transfer configuration used during the copy. See [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig){ target="_blank" } for all parameters

    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
    Assigns an IAM Bucket Policy to an S3 Bucket.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import S3BucketPolicyUtility

    s3_bucket_policy_utility = S3BucketPolicyUtility(
        bucket_name="YOUR-BUCKET-NAME",
        aws_access_key_id="YOUR-AWS-ACCESS-KEY",
        aws_secret_access_key="YOUR-AWS-SECRET-ACCESS-KEY",
        aws_session_token="YOUR-AWS-SESSION-TOKEN",
        sid="YOUD-SID",
        effect="EFFECT",
        principal="PRINCIPAL",
        action=["ACTIONS"],
        resource=["RESOURCES"]
    )

    result = s3_bucket_policy_utility.execute()
    ```

    Parameters:
        bucket_name (str): S3 Bucket Name
        aws_access_key_id (str): AWS Access Key
        aws_secret_access_key (str): AWS Secret Key
        aws_session_token (str): AWS Session Token
        sid (str): S3 Bucket Policy Sid to be updated
        effect (str): Effect to be applied to the policy
        principal (str): Principal to be applied to Policy
        action (list[str]): List of actions to be applied to the policy
        resource (list[str]): List of resources to be applied to the policy
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
    Sets configuration key value pairs to a Spark Session

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import SparkConfigurationUtility
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    configuration_utility = SparkConfigurationUtility(
        spark=spark,
        config={}
    )

    result = configuration_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        config (dict): Dictionary of spark configuration to be applied to the spark session
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        Executes configuration key value pairs to a Spark Session
    Creates a Delta Table in a Hive Metastore or in Databricks Unity Catalog.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.utilities.spark.delta_table_create import DeltaTableCreateUtility, DeltaTableColumn

    table_create_utility = DeltaTableCreateUtility(
        spark=spark_session,
        table_name="delta_table",
        columns=[
            DeltaTableColumn(name="EventDate", type="date", nullable=False, metadata={"delta.generationExpression": "CAST(EventTime AS DATE)"}),
            DeltaTableColumn(name="TagName", type="string", nullable=False),
            DeltaTableColumn(name="EventTime", type="timestamp", nullable=False),
            DeltaTableColumn(name="Status", type="string", nullable=True),
            DeltaTableColumn(name="Value", type="float", nullable=True)
        ],
        partitioned_by=["EventDate"],
        properties={"delta.logRetentionDuration": "7 days", "delta.enableChangeDataFeed": "true"},
        comment="Creation of Delta Table"
    )

    result = table_create_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        table_name (str): Name of the table, including catalog and schema if table is to be created in Unity Catalog
        columns (list[DeltaTableColumn]): List of columns and their related column properties
        partitioned_by (list[str], optional): List of column names to partition the table by
        location (str, optional): Path to storage location
        properties (dict, optional): Propoerties that can be specified for a Delta Table. Further information on the options available are [here](https://docs.databricks.com/delta/table-properties.html#delta-table-properties)
        comment (str, optional): Provides a comment on the table metadata


    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
    Creates or Gets a Spark Session and uses settings and libraries of the imported RTDIP components to populate the spark configuration and jars in the spark session.

    Call this component after all imports of the RTDIP components to ensure that the spark session is configured correctly.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    spark_session_utility = SparkConfigurationUtility(
        config={},
        module=None,
        remote=None
    )

    result = spark_session_utility.execute()
    ```

    Parameters:
        config (optional dict): Dictionary of spark configuration to be applied to the spark session
        module (optional str): Provide the module to use for imports of rtdip-sdk components. If not populated, it will use the calling module to check for imports
        remote (optional str): Specify the remote parameters if intending to use Spark Connect
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        To execute
    Configures Spark to Connect to an ADLS Gen 2 Storage Account using a Service Principal.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.utilities import SparkADLSGen2SPNConnectUtility
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    adls_gen2_connect_utility = SparkADLSGen2SPNConnectUtility(
        spark=spark,
        storage_account="YOUR-STORAGAE-ACCOUNT-NAME",
        tenant_id="YOUR-TENANT-ID",
        client_id="YOUR-CLIENT-ID",
        client_secret="YOUR-CLIENT-SECRET"
    )

    result = adls_gen2_connect_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        storage_account (str): Name of the ADLS Gen 2 Storage Account
        tenant_id (str): Tenant ID of the Service Principal
        client_id (str): Service Principal Client ID
        client_secret (str): Service Principal Client Secret
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        Executes spark configuration to connect to an ADLS Gen 2 Storage Account using a service principal
    [Vacuums](https://docs.delta.io/latest/delta-utility.html#-delta-vacuum) a Delta Table.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.utilities.spark.delta_table_vacuum import DeltaTableVacuumUtility

    table_vacuum_utility =  DeltaTableVacuumUtility(
        spark=spark_session,
        table_name="delta_table",
        retention_hours="168"
    )

    result = table_vacuum_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        table_name (str): Name of the table, including catalog and schema if table is to be created in Unity Catalog
        retention_hours (int, optional): Sets the retention threshold in hours.
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
    [Optimizes](https://docs.delta.io/latest/optimizations-oss.html) a Delta Table.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.utilities.spark.delta_table_optimize import DeltaTableOptimizeUtility

    table_optimize_utility = DeltaTableOptimizeUtility(
        spark=spark_session,
        table_name="delta_table",
        where="EventDate<=current_date()",
        zorder_by=["EventDate"]
    )

    result = table_optimize_utility.execute()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        table_name (str): Name of the table, including catalog and schema if table is to be created in Unity Catalog
        where (str, optional): Apply a partition filter to limit optimize to specific partitions. Example, "date='2021-11-18'" or "EventDate<=current_date()"
        zorder_by (list[str], optional): List of column names to zorder the table by. For more information, see [here.](https://docs.delta.io/latest/optimizations-oss.html#optimize-performance-with-file-management&language-python)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
    Converts a Spark Dataframe column containing a json string created by OPC Publisher to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import OPCPublisherOPCUAJsonToPCDMTransformer

    opc_publisher_opcua_json_to_pcdm_transformer = OPCPublisherOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        multiple_rows_per_message=True,
        status_null_value="Good",
        change_type_value="insert",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX"
        ],
        filter=None
    )

    result = opc_publisher_opcua_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with Json OPC UA data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        multiple_rows_per_message (optional bool): Each Dataframe Row contains an array of/multiple OPC UA messages. The list of Json will be exploded into rows in the Dataframe.
        status_null_value (optional str): If populated, will replace null values in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
        timestamp_formats (optional list[str]): Specifies the timestamp formats to be used for converting the timestamp string to a Timestamp Type. For more information on formats, refer to this [documentation.](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)
        filter (optional str): Enables providing a filter to the data which can be required in certain scenarios. For example, it would be possible to filter on IoT Hub Device Id and Module by providing a filter in SQL format such as `systemProperties.iothub-connection-device-id = "<Device Id>" AND systemProperties.iothub-connection-module-id = "<Module>"`
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        
    Converts a dataframe body column from a binary to a string.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import BinaryToStringTransformer

    binary_to_string_transformer = BinaryToStringTransformer(
        data=df,
        souce_column_name="body",
        target_column_name="body"
    )

    result = binary_to_string_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe to be transformed
        source_column_name (str): Spark Dataframe column containing the Binary data
        target_column_name (str): Spark Dataframe column name to be used for the String data
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the body column converted to string.
        
    Converts a Spark DataFrame column containing binaryFile parquet data to the Process Control Data Model.

    This DataFrame should contain a path and the binary data. Typically this can be done using the Autoloader source component and specify "binaryFile" as the format.

    For more information about the SSIP PI Batch Connector, please see [here.](https://bakerhughesc3.ai/oai-solution/shell-sensor-intelligence-platform/)

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import SSIPPIBinaryFileToPCDMTransformer

    ssip_pi_binary_file_to_pcdm_transformer = SSIPPIBinaryFileToPCDMTransformer(
        data=df
    )

    result = ssip_pi_binary_file_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): DataFrame containing the path and binaryFile data
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the provided Binary data convert to PCDM
        
    Converts a PySpark DataFrame to a Pandas DataFrame.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PySparkToPandasTransformer

    pyspark_to_pandas = PySparkToPandasTransformer(
        df=df
    )

    result = pyspark_to_pandas.transform()
    ```

    Parameters:
        df (DataFrame): PySpark DataFrame to be converted
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A Pandas dataframe converted from a PySpark DataFrame.
        
    Converts a Spark Dataframe in PCDM format to Honeywell APM format.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PCDMToHoneywellAPMTransformer

    pcdm_to_honeywell_apm_transformer = PCDMToHoneywellAPMTransformer(
        data=df,
        quality="Good",
        history_samples_per_message=1,
        compress_payload=True
    )

    result = pcdm_to_honeywell_apm_transformer.transform()
    ```

    Parameters:
        data (Dataframe): Spark Dataframe in PCDM format
        quality (str): Value for quality inside HistorySamples
        history_samples_per_message (int): The number of HistorySamples for each row in the DataFrame (Batch Only)
        compress_payload (bool): If True compresses CloudPlatformEvent with gzip compression
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with with rows in Honeywell APM format
        
    Base class for all the Raw to Meters Data Model Transformers.

    Meters Data Model requires two outputs:
        - `UsageData` : To store measurement(value) as timeseries data.
        - `MetaData` : To store meters related meta information.

    It supports the generation of both the outputs as they share some common properties.

    Parameters:
        spark (SparkSession): Spark Session instance.
        data (DataFrame): Dataframe containing the raw MISO data.
        output_type (str): Must be one of `usage` or `meta`.
        name (str): Set this to override default `name` column.
        description (str): Set this to override default `description` column.
        value_type (ValueType): Set this to override default `value_type` column.
        version (str): Set this to override default `version` column.
        series_id (str): Set this to override default `series_id` column.
        series_parent_id (str): Set this to override default `series_parent_id` column.
    
        Converts a Spark DataFrame structure into new structure based on the Target Schema.

        Returns: Nothing.

        
        Returns:
            DataFrame: A dataframe with the raw data converted into MDM.
        
    Converts a Spark Dataframe column containing a json string created by SEM to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import SEMJsonToPCDMTransformer

    sem_json_to_pcdm_transformer = SEMJsonToPCDMTransformer(
        data=df
        source_column_name="body",
        version=10,
        status_null_value="Good",
        change_type_value="insert"
    )

    result = sem_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with SEM data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        version (int): The version for the OBC field mappings. The latest version is 10.
        status_null_value (optional str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        
    Converts a Pandas DataFrame to a PySpark DataFrame.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PandasToPySparkTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pandas_to_pyspark = PandasToPySparkTransformer(
        spark=spark,
        df=df,
    )

    result = pandas_to_pyspark.transform()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to convert DataFrame
        df (DataFrame): Pandas DataFrame to be converted
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A PySpark dataframe converted from a Pandas DataFrame.
        
    Converts a Spark DataFrame containing Binary JSON data and related Properties to the Process Control Data Model

    For more information about the SSIP PI Streaming Connector, please see [here.](https://bakerhughesc3.ai/oai-solution/shell-sensor-intelligence-platform/)

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import SSIPPIJsonStreamToPCDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    ssip_pi_json_stream_to_pcdm_transformer = SSIPPIJsonStreamToPCDMTransformer(
        spark=spark,
        data=df,
        source_column_name="body",
        properties_column_name="",
        metadata_delta_table=None
    )

    result = ssip_pi_json_stream_to_pcdm_transformer.transform()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        data (DataFrame): DataFrame containing the path and binaryFile data
        source_column_name (str): Spark Dataframe column containing the Binary json data
        properties_column_name (str): Spark Dataframe struct typed column containing an element with the PointType
        metadata_delta_table (optional, str): Name of a metadata table that can be used for PointType mappings
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the provided Binary data converted to PCDM
        
    Converts a Spark Dataframe column containing a json string created by Fledge to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import FledgeOPCUAJsonToPCDMTransformer

    fledge_opcua_json_to_pcdm_transfromer = FledgeOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert",
        timestamp_formats=[
            "yyyy-MM-dd'T'HH:mm:ss.SSSX",
            "yyyy-MM-dd'T'HH:mm:ssX",
        ]
    )

    result = fledge_opcua_json_to_pcdm_transfromer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with Json Fledge data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        status_null_value (str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
        timestamp_formats (list[str]): Specifies the timestamp formats to be used for converting the timestamp string to a Timestamp Type. For more information on formats, refer to this [documentation.](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        
    Converts a Spark Dataframe column containing a json string created by Honeywell APM to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import HoneywellAPMJsonToPCDMTransformer

    honeywell_apm_json_to_pcdm_transformer = HoneywellAPMJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert"
    )

    result = honeywell_apm_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with EdgeX data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        status_null_value (optional str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        
    Converts a Spark Dataframe column containing a json string created by EdgeX to the Process Control Data Model.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import EdgeXOPCUAJsonToPCDMTransformer

    edge_opcua_json_to_pcdm_transformer = EdgeXOPCUAJsonToPCDMTransformer(
        data=df,
        souce_column_name="body",
        status_null_value="Good",
        change_type_value="insert"
    )

    result = edge_opcua_json_to_pcdm_transformer.transform()
    ```

    Parameters:
        data (DataFrame): Dataframe containing the column with EdgeX data
        source_column_name (str): Spark Dataframe column containing the OPC Publisher Json OPC UA data
        status_null_value (optional str): If populated, will replace 'Good' in the Status column with the specified value.
        change_type_value (optional str): If populated, will replace 'insert' in the ChangeType column with the specified value.
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Returns:
            DataFrame: A dataframe with the specified column converted to PCDM
        
    Extract a single point from a local .nc file downloaded from ECMWF via MARS

    Args:
        lat (float): Latitude of point to extract
        lon (float): Longitude of point to extract
        load_path (str): Path to local directory with nc files downloaded in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        run_frequency (str): Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
        utc (bool, optional): Add utc to the datetime indexes? Defaults to True.
    Extract a grid from a local .nc file downloaded from ECMWF via MARS

    Args:
        lat_min (float): Minimum latitude of grid to extract
        lat_max (float): Maximum latitude of grid to extract
        lon_min (float): Minimum longitude of grid to extract
        lon_max (float): Maximum longitude of grid to extract
        grid_step (float): The grid length to use to define the grid, e.g. 0.1.
        load_path (str): Path to local directory with nc files downloaded in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        run_frequency (str): Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
        utc (bool, optional): Add utc to the datetime indexes? Defaults to True.

    
    Base class for extracting forecast data downloaded in .nc format from ECMWF MARS Server.

    Args:
        load_path (str): Path to local directory where the nc files will be stored, in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        run_frequency (str):Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
        lat (DataArray): Latitude values to extract from nc files
        lon (DataArray): Longitude values to extract from nc files
        utc (bool = True): Whether to convert the time to UTC or not
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Converts the tag names of wind speed from the format used in the nc files to the format used in the weather data model.

        Args:
            x (list): List of variable names of raw tags to be extracted from the nc files

        Returns:
            new_tags(list): List of variable names of raw tags to be extracted from the nc files, converted to the format used in the weather data model.
        Extract raw data from stored nc filed downloaded via ECMWF MARS.

        Args:
            tag_prefix (str): Prefix of the tag names of raw tags to be added to the dataframe
            variables (list): List of variable names of raw tags to be extracted from the nc files
            method (str, optional): The method used to match latitude/longitude in xarray using .sel(), by default "nearest"

        Returns:
            df (pd.DataFrame): Raw data extracted with lat, lon, run_time, target_time as a pd.multiindex and variables as columns.
        
    Converts MISO Raw data into Meters Data Model.

    Please check the BaseRawToMDMTransformer for the required arguments and methods.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import MISOToMDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_to_mdm_transformer = MISOToMDMTransformer(
        spark=spark,
        data=df,
        output_type="usage",
        name=None,
        description=None,
        value_type=None,
        version=None,
        series_id=None,
        series_parent_id=None
    )

    result = miso_to_mdm_transformer.transform()
    ```

    BaseRawToMDMTransformer:
        ::: src.sdk.python.rtdip_sdk.pipelines.transformers.spark.base_raw_to_mdm
    
    Converts PJM Raw data into Meters Data Model.

    Please check the BaseRawToMDMTransformer for the required arguments and methods.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.transformers import PJMToMDMTransformer
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_to_mdm_transformer = PJMToMDMTransformer(
        spark=spark,
        data=df,
        output_type="usage",
        name=None,
        description=None,
        value_type=None,
        version=None,
        series_id=None,
        series_parent_id=None
    )

    result = pjm_to_mdm_transformer.transform()
    ```

    BaseRawToMDMTransformer:
        ::: src.sdk.python.rtdip_sdk.pipelines.transformers.spark.base_raw_to_mdm
    
    Converts a raw forecast into weather data model.

    Parameters:
        spark (SparkSession): Spark Session instance.
        data (DataFrame): Dataframe to be transformed
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Converts a Spark DataFrame structure into new structure based on the Target Schema.

        Returns: Nothing.

        
        Returns:
            DataFrame: A Forecast dataframe converted into Weather Data Model
        
    The Python Delta Sharing Source is used to read data from a Delta table with Delta Sharing configured, without using Apache Spark.

    Example
    -------
    ```python
    from rtdip_sdk.pipelines.sources import PythonDeltaSharingSource

    python_delta_sharing_source = PythonDeltaSharingSource(
        profile_path="{CREDENTIAL-FILE-LOCATION}",
        share_name="{SHARE-NAME}",
        schema_name="{SCHEMA-NAME}",
        table_name="{TABLE-NAME}"
    )

    python_delta_sharing_source.read_batch()
    ```

    Parameters:
        profile_path (str): Location of the credential file. Can be any URL supported by [FSSPEC](https://filesystem-spec.readthedocs.io/en/latest/index.html){ target="_blank" }
        share_name (str): The value of 'share=' for the table
        schema_name (str): The value of 'schema=' for the table
        table_name (str): The value of 'name=' for the table
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
        Reads data from a Delta table with Delta Sharing into a Polars LazyFrame.
        
        Raises:
            NotImplementedError: Reading from a Delta table with Delta Sharing using Python is only possible for batch reads.
        
    The Python Delta Source is used to read data from a Delta table without using Apache Spark, returning a Polars LazyFrame.

     Example
    --------
    === "Azure"

        ```python
        from rtdip_sdk.pipelines.sources import PythonDeltaSource

        path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}

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

        python_delta_source.read_batch()
        ```
    === "AWS"

        ```python
        from rtdip_sdk.pipelines.sources import PythonDeltaSource

        path = "https://s3.{REGION-CODE}.amazonaws.com/{BUCKET-NAME}/{KEY-NAME}"

        python_delta_source = PythonDeltaSource(
            path=path,
            version=None,
            storage_options={
                "aws_access_key_id": "{AWS-ACCESS-KEY-ID}",
                "aws_secret_access_key": "{AWS-SECRET-ACCESS-KEY}"
            },
            pyarrow_options=None,
            without_files=False
        )

        python_delta_source.read_batch()
        ```

    Parameters:
        path (str): Path to the Delta table. Can be local or in S3/Azure storage
        version (optional int): Specify the Delta table version to read from. Defaults to the latest version
        storage_options (optional dict): Used to read from AWS/Azure storage. For AWS use format {"aws_access_key_id": "<>", "aws_secret_access_key":"<>"}. For Azure use format {"azure_storage_account_name": "<>", "azure_storage_account_key": "<>"}.
        pyarrow_options (optional dict): Data Access and Efficiency options when reading from Delta. See [to_pyarrow_dataset](https://delta-io.github.io/delta-rs/python/api_reference.html#deltalake.table.DeltaTable.to_pyarrow_dataset){ target="_blank" }.
        without_files (optional bool): If True loads the table without tracking files
    
        Attributes:
            SystemType (Environment): Requires PYTHON
        
        Reads data from a Delta table into a Polars LazyFrame
        
        Raises:
            NotImplementedError: Reading from a Delta table using Python is only possible for batch reads. To perform a streaming read, use the read_stream method of the SparkDeltaSource component.
        
    This Spark source class is used to read batch or streaming data from an Eventhub using the Kafka protocol. This enables Eventhubs to be used as a source in applications like Delta Live Tables or Databricks Serverless Jobs as the Spark Eventhubs JAR is not supported in these scenarios.

    The dataframe returned is transformed to ensure the schema is as close to the Eventhub Spark source as possible. There are some minor differences:

    - `offset` is dependent on `x-opt-offset` being populated in the headers provided. If this is not found in the headers, the value will be null
    - `publisher` is dependent on `x-opt-publisher` being populated in the headers provided. If this is not found in the headers, the value will be null
    - `partitionKey` is dependent on `x-opt-partition-key` being populated in the headers provided. If this is not found in the headers, the value will be null
    - `systemProperties` are identified according to the list provided in the [Eventhub documentation](https://learn.microsoft.com/en-us/azure/data-explorer/ingest-data-event-hub-overview#event-system-properties-mapping){ target="_blank" } and [IoT Hub documentation](https://learn.microsoft.com/en-us/azure/data-explorer/ingest-data-iot-hub-overview#event-system-properties-mapping){ target="_blank" }

    Default settings will be specified if not provided in the `options` parameter:

    - `kafka.sasl.mechanism` will be set to `PLAIN`
    - `kafka.security.protocol` will be set to `SASL_SSL`
    - `kafka.request.timeout.ms` will be set to `60000`
    - `kafka.session.timeout.ms` will be set to `60000`

    Examples
    --------
    ```python
    #Kafka Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkKafkaEventhubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
    consumerGroup = "{YOUR-CONSUMER-GROUP}"

    kafka_eventhub_source = SparkKafkaEventhubSource(
        spark=spark,
        options={
            "startingOffsets": "earliest",
            "maxOffsetsPerTrigger": 10000,
            "failOnDataLoss": "false",
        },
        connection_string=connectionString,
        consumer_group="consumerGroup"
    )

    kafka_eventhub_source.read_stream()
    ```
    ```python
    #Kafka Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkKafkaEventhubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"
    consumerGroup = "{YOUR-CONSUMER-GROUP}"

    kafka_eventhub_source = SparkKafkaEventhubSource(
        spark=spark,
        options={
            "startingOffsets": "earliest",
            "endingOffsets": "latest",
            "failOnDataLoss": "false"
        },
        connection_string=connectionString,
        consumer_group="consumerGroup"
    )

    kafka_eventhub_source.read_batch()
    ```

    Required and optional configurations can be found in the Attributes and Parameter tables below.
    Additionally, there are more optional configurations which can be found [here.](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }

    Parameters:
        spark (SparkSession): Spark Session
        options (dict): A dictionary of Kafka configurations (See Attributes tables below). For more information on configuration options see [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }
        connection_string (str): Eventhubs connection string is required to connect to the Eventhubs service. This must include the Eventhub name as the `EntityPath` parameter. Example `"Endpoint=sb://test.servicebus.windows.net/;SharedAccessKeyName=test;SharedAccessKey=test_key;EntityPath=test_eventhub"`
        consumer_group (str): The Eventhub consumer group to use for the connection

    The only configuration that must be set for the Kafka source for both batch and streaming queries is listed below.

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port):  The Kafka "bootstrap.servers" configuration. (Streaming and Batch)

    There are multiple ways of specifying which topics to subscribe to. You should provide only one of these parameters:

    Attributes:
        assign (json string {"topicA"︰[0,1],"topicB"︰[2,4]}):  Specific TopicPartitions to consume. Only one of "assign", "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)
        subscribe (A comma-separated list of topics): The topic list to subscribe. Only one of "assign", "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)
        subscribePattern (Java regex string): The pattern used to subscribe to topic(s). Only one of "assign, "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)

    The following configurations are optional:

    Attributes:
        startingTimestamp (timestamp str): The start point of timestamp when a query is started, a string specifying a starting timestamp for all partitions in topics being subscribed. Please refer the note on starting timestamp offset options below. (Streaming and Batch)
        startingOffsetsByTimestamp (JSON str): The start point of timestamp when a query is started, a json string specifying a starting timestamp for each TopicPartition. Please refer the note on starting timestamp offset options below. (Streaming and Batch)
        startingOffsets ("earliest", "latest" (streaming only), or JSON string): The start point when a query is started, either "earliest" which is from the earliest offsets, "latest" which is just from the latest offsets, or a json string specifying a starting offset for each TopicPartition. In the json, -2 as an offset can be used to refer to earliest, -1 to latest.
        endingTimestamp (timestamp str): The end point when a batch query is ended, a json string specifying an ending timestamp for all partitions in topics being subscribed. Please refer the note on ending timestamp offset options below. (Batch)
        endingOffsetsByTimestamp (JSON str): The end point when a batch query is ended, a json string specifying an ending timestamp for each TopicPartition. Please refer the note on ending timestamp offset options below. (Batch)
        endingOffsets (latest or JSON str): The end point when a batch query is ended, either "latest" which is just referred to the latest, or a json string specifying an ending offset for each TopicPartition. In the json, -1 as an offset can be used to refer to latest, and -2 (earliest) as an offset is not allowed. (Batch)
        maxOffsetsPerTrigger (long): Rate limit on maximum number of offsets processed per trigger interval. The specified total number of offsets will be proportionally split across topicPartitions of different volume. (Streaming)
        minOffsetsPerTrigger (long): Minimum number of offsets to be processed per trigger interval. The specified total number of offsets will be proportionally split across topicPartitions of different volume. (Streaming)
        failOnDataLoss (bool): Whether to fail the query when it's possible that data is lost (e.g., topics are deleted, or offsets are out of range). This may be a false alarm. You can disable it when it doesn't work as you expected.
        minPartitions (int): Desired minimum number of partitions to read from Kafka. By default, Spark has a 1-1 mapping of topicPartitions to Spark partitions consuming from Kafka. (Streaming and Batch)
        includeHeaders (bool): Whether to include the Kafka headers in the row. (Streaming and Batch)

    !!! note "Starting Timestamp Offset Note"
        If Kafka doesn't return the matched offset, the behavior will follow to the value of the option <code>startingOffsetsByTimestampStrategy</code>.

        <code>startingTimestamp</code> takes precedence over <code>startingOffsetsByTimestamp</code> and </code>startingOffsets</code>.

        For streaming queries, this only applies when a new query is started, and that resuming will always pick up from where the query left off. Newly discovered partitions during a query will start at earliest.

    !!! note "Ending Timestamp Offset Note"
        If Kafka doesn't return the matched offset, the offset will be set to latest.

        <code>endingOffsetsByTimestamp</code> takes precedence over <code>endingOffsets</code>.

    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from Kafka.
        
        Reads streaming data from Kafka.
        
    This Spark source class is used to read batch or streaming data from Eventhubs. Eventhub configurations need to be specified as options in a dictionary.
    Additionally, there are more optional configurations which can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
    If using startingPosition or endingPosition make sure to check out the **Event Position** section for more details and examples.

    Example
    --------
    ```python
    #Eventhub Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkEventhubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility
    import json

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"

    startingEventPosition = {
    "offset": -1,
    "seqNo": -1,
    "enqueuedTime": None,
    "isInclusive": True
    }

    eventhub_source = SparkEventhubSource(
        spark=spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "maxEventsPerTrigger" : 1000
        }
    )

    eventhub_source.read_stream()
    ```
    ```python
     #Eventhub Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkEventhubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility
    import json

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"

    startingEventPosition = {
        "offset": -1,
        "seqNo": -1,
        "enqueuedTime": None,
        "isInclusive": True
    }

    endingEventPosition = {
        "offset": None,
        "seqNo": -1,
        "enqueuedTime": endTime,
        "isInclusive": True
    }

    eventhub_source = SparkEventhubSource(
        spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "eventhubs.endingPosition": json.dumps(endingEventPosition)
        }
    )

    eventhub_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        options (dict): A dictionary of Eventhub configurations (See Attributes table below)

    Attributes:
        eventhubs.connectionString (str):  Eventhubs connection string is required to connect to the Eventhubs service. (Streaming and Batch)
        eventhubs.consumerGroup (str): A consumer group is a view of an entire eventhub. Consumer groups enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their own offsets. (Streaming and Batch)
        eventhubs.startingPosition (JSON str): The starting position for your Structured Streaming job. If a specific EventPosition is not set for a partition using startingPositions, then we use the EventPosition set in startingPosition. If nothing is set in either option, we will begin consuming from the end of the partition. (Streaming and Batch)
        eventhubs.endingPosition: (JSON str): The ending position of a batch query. This works the same as startingPosition. (Batch)
        maxEventsPerTrigger (long): Rate limit on maximum number of events processed per trigger interval. The specified total number of events will be proportionally split across partitions of different volume. (Stream)

    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from Eventhubs.
        
        Reads streaming data from Eventhubs.
        
    The Spark Auto Loader is used to read new data files as they arrive in cloud storage. Further information on Auto Loader is available [here](https://docs.databricks.com/ingestion/auto-loader/index.html)

    Example
    --------
    === "ADLS Gen2"

        ```python
        from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
        from rtdip_sdk.pipelines.utilities import SparkSessionUtility

        # Not required if using Databricks
        spark = SparkSessionUtility(config={}).execute()

        options = {}
        path = "abfss://{FILE-SYSTEM}@{ACCOUNT-NAME}.dfs.core.windows.net/{PATH}/{FILE-NAME}
        format = "{DESIRED-FILE-FORMAT}"

        DataBricksAutoLoaderSource(spark, options, path, format).read_stream()

        OR

        DataBricksAutoLoaderSource(spark, options, path, format).read_batch()
        ```
    === "AWS S3"

        ```python
        from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
        from rtdip_sdk.pipelines.utilities import SparkSessionUtility

        # Not required if using Databricks
        spark = SparkSessionUtility(config={}).execute()

        options = {}
        path = "https://s3.{REGION-CODE}.amazonaws.com/{BUCKET-NAME}/{KEY-NAME}"
        format = "{DESIRED-FILE-FORMAT}"

        DataBricksAutoLoaderSource(spark, options, path, format).read_stream()

        OR

        DataBricksAutoLoaderSource(spark, options, path, format).read_batch()
        ```
    === "GCS"

        ```python
        from rtdip_sdk.pipelines.sources import DataBricksAutoLoaderSource
        from rtdip_sdk.pipelines.utilities import SparkSessionUtility

        # Not required if using Databricks
        spark = SparkSessionUtility(config={}).execute()

        options = {}
        path = "gs://{BUCKET-NAME}/{FILE-PATH}"
        format = "{DESIRED-FILE-FORMAT}"

        DataBricksAutoLoaderSource(spark, options, path, format).read_stream()

        OR

        DataBricksAutoLoaderSource(spark, options, path, format).read_batch()
        ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from cloud storage
        options (dict): Options that can be specified for configuring the Auto Loader. Further information on the options available are [here](https://docs.databricks.com/ingestion/auto-loader/options.html)
        path (str): The cloud storage path
        format (str): Specifies the file format to be read. Supported formats are available [here](https://docs.databricks.com/ingestion/auto-loader/options.html#file-format-options)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK on Databricks
        
        Raises:
            NotImplementedError: Auto Loader only supports streaming reads. To perform a batch read, use the read_stream method of this component and specify the Trigger on the write_stream to be `availableNow` to perform batch-like reads of cloud storage files.
        
        Performs streaming reads of files in cloud storage.
        
    The Spark Kinesis Source is used to read data from Kinesis in a Databricks environment.
    Structured streaming from Kinesis is **not** supported in open source Spark.

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import SparkKinesisSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    kinesis_source = SparkKinesisSource(
        spark=spark,
        options={
            "awsAccessKey": "{AWS-ACCESS-KEY}",
            "awsSecretKey": "{AWS-SECRET-KEY}",
            "streamName": "{STREAM-NAME}",
            "region": "{REGION}",
            "endpoint": "https://kinesis.{REGION}.amazonaws.com",
            "initialPosition": "earliest"
        }
    )

    kinesis_source.read_stream()

    OR

    kinesis_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from Kinesis
        options (dict): Options that can be specified for a Kinesis read operation (See Attributes table below). Further information on the options is available [here](https://docs.databricks.com/structured-streaming/kinesis.html#configuration){ target="_blank" }

    Attributes:
        awsAccessKey (str): AWS access key.
        awsSecretKey (str): AWS secret access key corresponding to the access key.
        streamName (List[str]): The stream names to subscribe to.
        region (str): The region the streams are defined in.
        endpoint (str): The regional endpoint for Kinesis Data Streams.
        initialPosition (str): The point to start reading from; earliest, latest, or at_timestamp.
    
        Attributes:
            SystemType (Environment): Requires PYSPARK_DATABRICKS
        
        Raises:
            NotImplementedError: Kinesis only supports streaming reads. To perform a batch read, use the read_stream method of this component and specify the Trigger on the write_stream to be `availableNow=True` to perform batch-like reads of cloud storage files.
        
        Reads streaming data from Kinesis. All of the data in the table is processed as well as any new data that arrives after the stream started.
        
    The Spark Delta Sharing Source is used to read data from a Delta table where Delta sharing is configured

    Example
    --------
    ```python
    #Delta Sharing Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSharingSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_sharing_source = SparkDeltaSharingSource(
        spark=spark,
        options={
            "maxFilesPerTrigger": 1000,
            "ignoreChanges: True,
            "startingVersion": 0
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_sharing_source.read_stream()
    ```
    ```python
    #Delta Sharing Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSharingSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_sharing_source = SparkDeltaSharingSource(
        spark=spark,
        options={
            "versionAsOf": 0,
            "timestampAsOf": "yyyy-mm-dd hh:mm:ss[.fffffffff]"
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_sharing_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from a Delta table
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available [here](https://docs.databricks.com/data-sharing/read-data-open.html#apache-spark-read-shared-data){ target="_blank" }
        table_path (str): Path to credentials file and Delta table to query

    Attributes:
        ignoreDeletes (bool str): Ignore transactions that delete data at partition boundaries. (Streaming)
        ignoreChanges (bool str): Pre-process updates if files had to be rewritten in the source table due to a data changing operation. (Streaming)
        startingVersion (int str): The Delta Lake version to start from. (Streaming)
        startingTimestamp (datetime str): The timestamp to start from. (Streaming)
        maxFilesPerTrigger (int): How many new files to be considered in every micro-batch. The default is 1000. (Streaming)
        maxBytesPerTrigger (int): How much data gets processed in each micro-batch. (Streaming)
        readChangeFeed (bool str): Stream read the change data feed of the shared table. (Batch & Streaming)
        timestampAsOf (datetime str): Query the Delta Table from a specific point in time. (Batch)
        versionAsOf (int str): Query the Delta Table from a specific version. (Batch)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from Delta. Most of the options provided by the Apache Spark DataFrame read API are supported for performing batch reads on Delta tables.
        
        Reads streaming data from Delta. All of the data in the table is processed as well as any new data that arrives after the stream started. .load() can take table name or path.
        
    This Spark source class is used to read batch or streaming data from an IoT Hub. IoT Hub configurations need to be specified as options in a dictionary.
    Additionally, there are more optional configurations which can be found [here.](https://github.com/Azure/azure-event-hubs-spark/blob/master/docs/PySpark/structured-streaming-pyspark.md#event-hubs-configuration){ target="_blank" }
    If using startingPosition or endingPosition make sure to check out the **Event Position** section for more details and examples.

    Example
    --------
    ```python
    #IoT Hub Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkIoThubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility
    import json

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"

    startingEventPosition = {
    "offset": -1,
    "seqNo": -1,
    "enqueuedTime": None,
    "isInclusive": True
    }

    iot_hub_source = SparkIoThubSource(
        spark=spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "maxEventsPerTrigger" : 1000
        }
    )

    iot_hub_source.read_stream()
    ```
    ```python
     #IoT Hub Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkIoThubSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility
    import json

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    connectionString = "Endpoint=sb://{NAMESPACE}.servicebus.windows.net/;SharedAccessKeyName={ACCESS_KEY_NAME};SharedAccessKey={ACCESS_KEY}=;EntityPath={EVENT_HUB_NAME}"

    startingEventPosition = {
        "offset": -1,
        "seqNo": -1,
        "enqueuedTime": None,
        "isInclusive": True
    }

    endingEventPosition = {
        "offset": None,
        "seqNo": -1,
        "enqueuedTime": endTime,
        "isInclusive": True
    }

    iot_hub_source = SparkIoThubSource(
        spark,
        options = {
            "eventhubs.connectionString": connectionString,
            "eventhubs.consumerGroup": "{YOUR-CONSUMER-GROUP}",
            "eventhubs.startingPosition": json.dumps(startingEventPosition),
            "eventhubs.endingPosition": json.dumps(endingEventPosition)
        }
    )

    iot_hub_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        options (dict): A dictionary of IoT Hub configurations (See Attributes table below)

    Attributes:
        eventhubs.connectionString (str):  IoT Hub connection string is required to connect to the Eventhubs service. (Streaming and Batch)
        eventhubs.consumerGroup (str): A consumer group is a view of an entire IoT Hub. Consumer groups enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their own offsets. (Streaming and Batch)
        eventhubs.startingPosition (JSON str): The starting position for your Structured Streaming job. If a specific EventPosition is not set for a partition using startingPositions, then we use the EventPosition set in startingPosition. If nothing is set in either option, we will begin consuming from the end of the partition. (Streaming and Batch)
        eventhubs.endingPosition: (JSON str): The ending position of a batch query. This works the same as startingPosition. (Batch)
        maxEventsPerTrigger (long): Rate limit on maximum number of events processed per trigger interval. The specified total number of events will be proportionally split across partitions of different volume. (Stream)

    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from IoT Hubs.
        
        Reads streaming data from IoT Hubs.
        
    This Spark source class is used to read batch or streaming data from Kafka. Required and optional configurations can be found in the Attributes tables below.

    Additionally, there are more optional configurations which can be found [here.](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }

    Example
    --------
    ```python
     #Kafka Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkKafkaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    kafka_source = SparkKafkaSource(
        spark=spark,
        options={
            "kafka.bootstrap.servers": "{HOST_1}:{PORT_1},{HOST_2}:{PORT_2}",
            "subscribe": "{TOPIC_1},{TOPIC_2}",
            "includeHeaders", "true"
        }
    )

    kafka_source.read_stream()
    ```
    ```python
     #Kafka Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkKafkaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    kafka_source = SparkKafkaSource(
        spark=spark,
        options={
            "kafka.bootstrap.servers": "{HOST_1}:{PORT_1},{HOST_2}:{PORT_2}",
            "subscribe": "{TOPIC_1},{TOPIC_2}",
            "startingOffsets": "earliest",
            "endingOffsets": "latest"
        }
    )

    kafka_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session
        options (dict): A dictionary of Kafka configurations (See Attributes tables below). For more information on configuration options see [here](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html){ target="_blank" }

    The following attributes are the most common configurations for Kafka.

    The only configuration that must be set for the Kafka source for both batch and streaming queries is listed below.

    Attributes:
        kafka.bootstrap.servers (A comma-separated list of host︰port):  The Kafka "bootstrap.servers" configuration. (Streaming and Batch)

    There are multiple ways of specifying which topics to subscribe to. You should provide only one of these attributes:

    Attributes:
        assign (json string {"topicA"︰[0,1],"topicB"︰[2,4]}):  Specific TopicPartitions to consume. Only one of "assign", "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)
        subscribe (A comma-separated list of topics): The topic list to subscribe. Only one of "assign", "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)
        subscribePattern (Java regex string): The pattern used to subscribe to topic(s). Only one of "assign, "subscribe" or "subscribePattern" options can be specified for Kafka source. (Streaming and Batch)

    The following configurations are optional:

    Attributes:
        startingTimestamp (timestamp str): The start point of timestamp when a query is started, a string specifying a starting timestamp for all partitions in topics being subscribed. Please refer the note on starting timestamp offset options below. (Streaming and Batch)
        startingOffsetsByTimestamp (JSON str): The start point of timestamp when a query is started, a json string specifying a starting timestamp for each TopicPartition. Please refer the note on starting timestamp offset options below. (Streaming and Batch)
        startingOffsets ("earliest", "latest" (streaming only), or JSON string): The start point when a query is started, either "earliest" which is from the earliest offsets, "latest" which is just from the latest offsets, or a json string specifying a starting offset for each TopicPartition. In the json, -2 as an offset can be used to refer to earliest, -1 to latest.
        endingTimestamp (timestamp str): The end point when a batch query is ended, a json string specifying an ending timestamp for all partitions in topics being subscribed. Please refer the note on ending timestamp offset options below. (Batch)
        endingOffsetsByTimestamp (JSON str): The end point when a batch query is ended, a json string specifying an ending timestamp for each TopicPartition. Please refer the note on ending timestamp offset options below. (Batch)
        endingOffsets (latest or JSON str): The end point when a batch query is ended, either "latest" which is just referred to the latest, or a json string specifying an ending offset for each TopicPartition. In the json, -1 as an offset can be used to refer to latest, and -2 (earliest) as an offset is not allowed. (Batch)
        maxOffsetsPerTrigger (long): Rate limit on maximum number of offsets processed per trigger interval. The specified total number of offsets will be proportionally split across topicPartitions of different volume. (Streaming)
        minOffsetsPerTrigger (long): Minimum number of offsets to be processed per trigger interval. The specified total number of offsets will be proportionally split across topicPartitions of different volume. (Streaming)
        failOnDataLoss (bool): Whether to fail the query when it's possible that data is lost (e.g., topics are deleted, or offsets are out of range). This may be a false alarm. You can disable it when it doesn't work as you expected.
        minPartitions (int): Desired minimum number of partitions to read from Kafka. By default, Spark has a 1-1 mapping of topicPartitions to Spark partitions consuming from Kafka. (Streaming and Batch)
        includeHeaders (bool): Whether to include the Kafka headers in the row. (Streaming and Batch)

    !!! note "Starting Timestamp Offset Note"
        If Kafka doesn't return the matched offset, the behavior will follow to the value of the option <code>startingOffsetsByTimestampStrategy</code>.

        <code>startingTimestamp</code> takes precedence over <code>startingOffsetsByTimestamp</code> and </code>startingOffsets</code>.

        For streaming queries, this only applies when a new query is started, and that resuming will always pick up from where the query left off. Newly discovered partitions during a query will start at earliest.

    !!! note "Ending Timestamp Offset Note"
        If Kafka doesn't return the matched offset, the offset will be set to latest.

        <code>endingOffsetsByTimestamp</code> takes precedence over <code>endingOffsets</code>.

    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from Kafka.
        
        Reads streaming data from Kafka.
        
    The Spark Delta Source is used to read data from a Delta table.

    Example
    --------
    ```python
    #Delta Source for Streaming Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_source = SparkDeltaSource(
        spark=spark,
        options={
            "maxFilesPerTrigger": 1000,
            "ignoreChanges: True,
            "startingVersion": 0
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_source.read_stream()
    ```
    ```python
    #Delta Source for Batch Queries

    from rtdip_sdk.pipelines.sources import SparkDeltaSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    delta_source = SparkDeltaSource(
        spark=spark,
        options={
            "versionAsOf": 0,
            "timestampAsOf": "yyyy-mm-dd hh:mm:ss[.fffffffff]"
        },
        table_name="{YOUR-DELTA-TABLE-PATH}"
    )

    delta_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session required to read data from a Delta table.
        options (dict): Options that can be specified for a Delta Table read operation (See Attributes table below). Further information on the options is available for [batch](https://docs.delta.io/latest/delta-batch.html#read-a-table){ target="_blank" } and [streaming](https://docs.delta.io/latest/delta-streaming.html#delta-table-as-a-source){ target="_blank" }.
        table_name (str): Name of the Hive Metastore or Unity Catalog Delta Table

    Attributes:
        maxFilesPerTrigger (int): How many new files to be considered in every micro-batch. The default is 1000. (Streaming)
        maxBytesPerTrigger (int): How much data gets processed in each micro-batch. (Streaming)
        ignoreDeletes (bool str): Ignore transactions that delete data at partition boundaries. (Streaming)
        ignoreChanges (bool str): Pre-process updates if files had to be rewritten in the source table due to a data changing operation. (Streaming)
        startingVersion (int str): The Delta Lake version to start from. (Streaming)
        startingTimestamp (datetime str): The timestamp to start from. (Streaming)
        withEventTimeOrder (bool str): Whether the initial snapshot should be processed with event time order. (Streaming)
        timestampAsOf (datetime str): Query the Delta Table from a specific point in time. (Batch)
        versionAsOf (int str): Query the Delta Table from a specific version. (Batch)
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Reads batch data from Delta. Most of the options provided by the Apache Spark DataFrame read API are supported for performing batch reads on Delta tables.
        
        Reads streaming data from Delta. All of the data in the table is processed as well as any new data that arrives after the stream started. .load() can take table name or path.
        
    The Weather Forecast API V1 Source class to doownload nc files from ECMWF MARS server using the ECMWF python API.

    Parameters:
        spark (SparkSession): Spark Session instance
        save_path (str): Path to local directory where the nc files will be stored, in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format    date_end:str,
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        ecmwf_class (str): ecmwf classification of data
        stream (str): Operational model stream
        expver (str): Version of data
        leveltype (str): Surface level forecasts
        ec_vars (list): Variables of forecast measurements.
        forecast_area (list): N/W/S/E coordinates of the forecast area
        ecmwf_api_key (str): API key for ECMWF API
        ecmwf_api_email (str): Email for ECMWF API
    
        Attributes:
            SystemType (Environment): Requires PYSPARK
        
        Lead time for the forecast data.
        90 hours - 1 Hour Interval
        90-146 - 3 Hour interval
        146 -246 - 6 Hour interval

        Returns:
            lead_times: Lead times in an array format.
        
        API parameters for the forecast data.

        Returns:
            params (dict): API parameters for the forecast data.
        
        Pulls data from the Weather API and returns as .nc files.

        
    Download nc files from ECMWF MARS server using the ECMWF python API.
    Data is downloaded in parallel using joblib from ECMWF MARS server using the ECMWF python API.

    Parameters:
        save_path (str): Path to local directory where the nc files will be stored, in format "yyyy-mm-dd_HH.nc"
        date_start (str): Start date of extraction in "YYYY-MM-DD HH:MM:SS" format
        date_end (str): End date of extraction in "YYYY-MM-DD HH:MM:SS" format
        ecmwf_api_key (str): API key for ECMWF MARS server
        ecmwf_api_email (str): Email for ECMWF MARS server
        ecmwf_api_url (str): URL for ECMWF MARS server
        run_frequency (str):Frequency format of runs to download, e.g. "H"
        run_interval (str): Interval of runs, e.g. a run_frequency of "H" and run_interval of "12" will extract the data of the 00 and 12 run for each day.
    Retrieve the data from the server.

        Function will use the ecmwf api to download the data from the server.
        Note that mars has a max of two active requests per user and 20 queued
        requests.
        Data is downloaded in parallel using joblib from ECMWF MARS server using the ECMWF python API.


        Parameters:
            mars_dict (dict): Dictionary of mars parameters.
            n_jobs (int, optional): Download in parallel? by default None, i.e. no parallelization
            backend (str, optional) : Specify the parallelization backend implementation in joblib, by default "loky"
            tries (int, optional): Number of tries for each request if it fails, by default 5
            cost (bool, optional):  Pass a cost request to mars to estimate the size and efficiency of your request,
                but not actually download the data. Can be useful for defining requests,
                by default False.
        
        Return info on each ECMWF request.

        Returns:
            pd.Series: Successful request for each run == 1.
        
    The MISO Daily Load ISO Source is used to read daily load data from MISO API. It supports both Actual and Forecast data.

    API: <a href="https://docs.misoenergy.org/marketreports/">https://docs.misoenergy.org/marketreports/</a>

    Actual data is available for one day minus from the given date.

    Forecast data is available for next 6 day (inclusive of given date).

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import MISODailyLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_source = MISODailyLoadISOSource(
        spark=spark,
        options={
            "load_type": "actual",
            "date": "20230520",
        }
    )

    miso_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        load_type (str): Must be one of `actual` or `forecast`
        date (str): Must be in `YYYYMMDD` format.

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    
        Pulls data from the MISO API and parses the Excel file.

        Returns:
            Raw form of data.
        
        Creates a new `date_time` column and removes null values.

        Args:
            df: Raw form of data received from the API.

        Returns:
            Data after basic transformations.

        
        Filter outs Actual or Forecast data based on `load_type`.
        Args:
            df: Data received after preparation.

        Returns:
            Final data either containing Actual or Forecast values.

        
        Validates the following options:
            - `date` must be in the correct format.
            - `load_type` must be valid.

        Returns:
            True if all looks good otherwise raises Exception.

        
    The PJM Historical Load ISO Source is used to read historical load data from PJM API.

    API:               <a href="https://api.pjm.com/api/v1/">https://api.pjm.com/api/v1/</a>  (must be a valid apy key from PJM)

    Historical doc:    <a href="https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition">https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition</a>

    Historical is the same PJM endpoint as Actual, but is called repeatedly within a range established by the start_date & end_date attributes

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import PJMHistoricalLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_source = PJMHistoricalLoadISOSource(
        spark=spark,
        options={
            "api_key": "{api_key}",
            "start_date": "20230510",
            "end_date": "20230520",
        }
    )

    pjm_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        api_key (str): Must be a valid key from PJM, see PJM documentation
        start_date (str): Must be in `YYYY-MM-DD` format.
        end_date (str): Must be in `YYYY-MM-DD` format.

        query_batch_days (int): (optional) Number of days must be < 160 as per PJM & is defaulted to `120`
        sleep_duration (int): (optional) Number of seconds to sleep between request, defaulted to `5` seconds, used to manage requests to PJM endpoint
        request_count (int): (optional) Number of requests made to PJM endpoint before sleep_duration, currently defaulted to `1`

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
        Pulls data from the PJM API and parses the return including date ranges.

        Returns:
            Raw form of data.
        
        Validates all parameters including the following examples:
            - `start_date` & `end_data` must be in the correct format.
            - `start_date` must be behind `end_data`.
            - `start_date` must not be in the future (UTC).

        Returns:
            True if all looks good otherwise raises Exception.

        
    Base class for all the ISO Sources. It provides common functionality and helps in reducing the code redundancy.

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations
    
        Gets data from external ISO API.

        Args:
            url_suffix: String to be used as suffix to iso url.

        Returns:
            Raw content of the data received.

        
        Converts string datetime into Python datetime object with configured format and timezone.
        Args:
            datetime_str: String to be converted into datetime.

        Returns: Timezone aware datetime object.

        
        Hits the fetch_from_url method with certain parameters to get raw data from API.

        All the children ISO classes must override this method and call the fetch_url method
        in it.

        Returns:
             Raw DataFrame from API.
        
        Performs all the basic transformations to prepare data for further processing.
        All the children ISO classes must override this method.

        Args:
            df: Raw DataFrame, received from the API.

        Returns:
             Modified DataFrame, ready for basic use.

        
        Another data transformation helper method to be called after prepare data.
        Used for advance data processing such as cleaning, filtering, restructuring.
        All the children ISO classes must override this method if there is any post-processing required.

        Args:
            df: Initial modified version of DataFrame, received after preparing the data.

        Returns:
             Final version of data after all the fixes and modifications.

        
        Entrypoint method to return the final version of DataFrame.

        Returns:
            Modified form of data for specific use case.

        
        Performs all the options checks. Raises exception in case of any invalid value.
        Returns:
             True if all checks are passed.

        
        Ensures all the required options are provided and performs other validations.
        Returns:
             True if all checks are passed.

        
        Spark entrypoint, It executes the entire process of pulling, transforming & fixing data.
        Returns:
             Final Spark DataFrame converted from Pandas DataFrame post-execution.

        
        By default, the streaming operation is not supported but child classes can override if ISO supports streaming.

        Returns:
             Final Spark DataFrame after all the processing.

        
    The MISO Historical Load ISO Source is used to read historical load data from MISO API.

    API: <a href="https://docs.misoenergy.org/marketreports/">https://docs.misoenergy.org/marketreports/</a>

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import MISOHistoricalLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    miso_source = MISOHistoricalLoadISOSource(
        spark=spark,
        options={
            "start_date": "20230510",
            "end_date": "20230520",
        }
    )

    miso_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        start_date (str): Must be in `YYYYMMDD` format.
        end_date (str): Must be in `YYYYMMDD` format.
        fill_missing (str): Set to `"true"` to fill missing Actual load with Forecast load. Default - `true`.

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    
        Pulls data from the MISO API and parses the Excel file.

        Returns:
            Raw form of data.
        
        Creates a new `Datetime` column, removes null values and pivots the data.

        Args:
            df: Raw form of data received from the API.

        Returns:
            Data after basic transformations and pivoting.

        
        Filter outs data outside the requested date range.

        Args:
            df: Data received after preparation.

        Returns:
            Final data after all the transformations.

        
        Validates the following options:
            - `start_date` & `end_data` must be in the correct format.
            - `start_date` must be behind `end_data`.
            - `start_date` must not be in the future (UTC).

        Returns:
            True if all looks good otherwise raises Exception.

        
    The PJM Daily Load ISO Source is used to read daily load data from PJM API. It supports both Actual and Forecast data. Actual will return 1 day, Forecast will return 7 days

    API:           <a href="https://api.pjm.com/api/v1/">https://api.pjm.com/api/v1/</a>  (must be a valid apy key from PJM)

    Actual doc:    <a href="https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition">https://dataminer2.pjm.com/feed/ops_sum_prev_period/definition</a>

    Forecast doc:  <a href="https://dataminer2.pjm.com/feed/load_frcstd_7_day/definition">https://dataminer2.pjm.com/feed/load_frcstd_7_day/definition</a>

    Example
    --------
    ```python
    from rtdip_sdk.pipelines.sources import PJMDailyLoadISOSource
    from rtdip_sdk.pipelines.utilities import SparkSessionUtility

    # Not required if using Databricks
    spark = SparkSessionUtility(config={}).execute()

    pjm_source = PJMDailyLoadISOSource(
        spark=spark,
        options={
            "api_key": "{api_key}",
            "load_type": "actual"
        }
    )

    pjm_source.read_batch()
    ```

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below)

    Attributes:
        api_key (str): Must be a valid key from PJM, see api url
        load_type (str): Must be one of `actual` or `forecast`

    Please check the BaseISOSource for available methods.

    BaseISOSource:
        ::: src.sdk.python.rtdip_sdk.pipelines.sources.spark.iso.base_iso
    
        Gets data from external ISO API.

        Args:
            url_suffix: String to be used as suffix to iso url.

        Returns:
            Raw content of the data received.
        
        Pulls data from the PJM API and parses the return.

        Returns:
            Raw form of data.
        
        Creates a new date time column and removes null values. Renames columns

        Args:
            df: Raw form of data received from the API.

        Returns:
            Data after basic transformations.

        
        Validates the following options:
            - `load_type` must be valid.

        Returns:
            True if all looks good otherwise raises Exception.
        
    The Weather Forecast API V1 Source is used to read 15 days forecast from the Weather API.

    URL: <a href="https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json">
    https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json</a>

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below).

    Attributes:
        lat (str): Latitude of the Weather Station.
        lon (str): Longitude of the Weather Station.
        api_key (str): Weather API key.
        language (str): API response language. Defaults to `en-US`.
        units (str): Unit of measurements. Defaults to `e`.
    
        Prepares weather data for the use.

        Args:
            df: Data received after preparation.

        Returns:
            Final data after all the transformations.

        
        Pulls data from the Weather API and parses the JSON file.

        Returns:
            Raw form of data.
        
    The Weather Forecast API V1 Multi Source is used to read 15 days forecast from the Weather API. It allows to
    pull weather data for multiple stations and returns all of them in a single DataFrame.

    URL for one station: <a href="https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json">
    https://api.weather.com/v1/geocode/32.3667/-95.4/forecast/hourly/360hour.json</a>

    It takes a list of Weather Stations. Each station item must contain comma separated Latitude & Longitude.

    Examples
    --------
    `["32.3667,-95.4", "51.52,-0.11"]`

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of ISO Source specific configurations (See Attributes table below).

    Attributes:
        stations (list[str]): List of Weather Stations.
        api_key (str): Weather API key.
        language (str): API response language. Defaults to `en-US`.
        units (str): Unit of measurements. Defaults to `e`.
    
        Pulls data from the Weather API and parses the JSON file for multiple stations

        Returns:
            Raw form of data.
        
    Base class for all the Weather related sources. Provides common functionality.

    Parameters:
        spark (SparkSession): Spark Session instance
        options (dict): A dictionary of Weather Source specific configurations.

    
        Gets data from external Weather Forecast API.

        Args:
            url_suffix: String to be used as suffix to weather url.

        Returns:
            Raw content of the data received.

        
    Executes Pipeline components in their intended order as a complete data pipeline. It ensures that components dependencies are injected as needed.

    Parameters:
        job (PipelineJob): Contains the steps and tasks of a PipelineJob to be executed
        batch_job (bool): Specifies if the job is to be executed as a batch job
    
        Orders tasks within a job
        
        Orders steps within a task
        
        Determines the dependencies to be injected into each component
        
        Executes all the steps and tasks in a pipeline job as per the job definition.
        Container for pipeline configs.Container for pipeline clients.