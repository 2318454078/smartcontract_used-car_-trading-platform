# from web3 import Web3
# from solcx import compile_source
# import json


# class CarContrast():

#     def __init__(self):
#         self.w3 = Web3(Web3.EthereumTesterProvider())
#         self.w3.eth.default_account = self.w3.eth.accounts[0]
        
#     def new(self, info):
#         '''
#             新建合约
#         '''
#         print('contrast creating start')
#         data = json.dumps(info)
#         compiled_sol = compile_source(
#             '''
#             pragma solidity >0.5.0;

#             contract Checker {
#                 string public info;

#                 constructor(string memory _info) public {
#                     info = _info;
#                 }

#                 function getInfo() view public returns (string memory){
#                     return info;
#                 }
#             }
#             ''',
#             output_values=['abi', 'bin']
#         )
        
#         contract_id, contract_interface = compiled_sol.popitem()
#         bytecode = contract_interface['bin']
#         abi = contract_interface['abi']
#         Checker = self.w3.eth.contract(abi=abi, bytecode=bytecode)
#         tx_hash = Checker.constructor(data).transact()
#         tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
#         address = tx_receipt.contractAddress

#         self.abi = abi
#         print('contrast address: ', address)
#         Checker = self.w3.eth.contract(
#             address=address,
#             abi=self.abi,
#         )
#         print('contrast info: ', Checker.functions.getInfo().call())
#         print('contrast creating end')
#         print()
#         return address
    
#     def getInfo(self, address):
#         '''
#             获取address上的合约内容
#         '''
#         Checker = self.w3.eth.contract(
#             address=address,
#             abi=self.abi,
#         )
#         data = Checker.functions.getInfo().call()
#         info = json.loads(data)
#         return info


import json

class CarContrast():

    def __init__(self):
        self.database = {}
        self.address = 0
        
    def new(self, info):
        '''
            新建合约
        '''
        print('contrast creating start')
        address = self.address
        self.address = self.address + 1
        data = json.dumps(info)
        self.database[address] = data

        print('contrast address: ', address)        
        print('contrast info: ', info)
        print('contrast creating end')
        print()
        return address
    
    def getInfo(self, address):
        '''
            获取address上的合约内容
        '''
        data = self.database[address]
        info = json.loads(data)
        return info