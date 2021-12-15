from web3 import Web3, contract
from dotenv import load_dotenv
import os
import json
import sys

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("HTTPS_RPC_URL")))
with open('abi.json') as abi:
    ERC20_ABI = json.load(abi)

# This Class is not fully ERC20 Token defined
# This class contains only Read Function due to cost for Write Functin Cost Checking

class ERC20Contract:
    def __init__(self, addr):
        if not Web3.isAddress(addr):
            sys.stderr.write('Invalid Contract Address\n')
            sys.exit(2)

        try:
            self.contract = w3.eth.contract(address=addr, abi=ERC20_ABI)
            self.name = self.contract.functions.name().call()
            self.symbol = self.contract.functions.symbol().call()
            self.decimals = self.contract.functions.decimals().call()
            self.totalSupply = self.contract.functions.totalSupply().call()
        except:
            sys.stderr.write('Invalid Contract Type\n')
            sys.exit(2)

