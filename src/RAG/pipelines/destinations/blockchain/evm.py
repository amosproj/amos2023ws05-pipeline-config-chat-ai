"""
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
    """
"""
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
        """
"""
        Raises:
            NotImplementedError: Write stream is not supported.
        """