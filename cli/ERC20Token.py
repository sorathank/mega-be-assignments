from web3 import Web3, contract
from dotenv import load_dotenv
import os
import json

load_dotenv()

web3 = Web3(Web3.HTTPProvider(os.getenv("HTTPS_RPC_URL")))
with open('abi.json') as abi:
    ERC20_ABI = json.load(abi)

# This Class is not fully ERC20 Token defined
# This class contains only Read Function due to cost for Write Functin Cost Checking

class ERC20Contract:
    name = None
    symbol = None
    decimals = None
    contract = None

    def __init__(self, addr):
        self.contract = web3.eth.contract(address=addr, abi=ERC20_ABI)
        try:
            self.name = self.contract.functions.name().call()
            self.symbol = self.contract.functions.symbol().call()
            self.decimals = self.contract.functions.decimals().call()
        except:
            pass

