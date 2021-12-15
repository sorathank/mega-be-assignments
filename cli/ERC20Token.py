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
        addr = Web3.toChecksumAddress(addr)
        self.contract = w3.eth.contract(address=addr, abi=ERC20_ABI)
        try:
            self.name = self.contract.functions.name().call()
            self.symbol = self.contract.functions.symbol().call()
            self.decimals = self.contract.functions.decimals().call()
            self.totalSupply = self.contract.functions.totalSupply().call()
        except:
            sys.stderr.write('Invalid Contract Type\n')
            sys.exit(2)
    
    def uint2decimal(self, value):
        if value == 0: 
            decimal = 0
        
        ### EX. value = 100, self.decimals = 4 => decimal = "0.0100"  
        elif len(str(value)) <= self.decimals:
            decimal = f'0.{"0"*(self.decimals - len(str(value)))}{value}'

        ### EX. value = 1000, self.decimals = 2 => decimal = "10.00" 
        else:
            decimal = str(value)[:len(str(value)) - self.decimals] + '.' + str(value)[len(str(value)) - self.decimals:]
            
        return float(decimal)

    def balanceOf(self, addr):
        if not Web3.isAddress(addr):
            sys.stderr.write('Invalid Tartget Address\n')
            sys.exit(2)
        balance = self.contract.functions.balanceOf(addr).call()
        return f'Balance of {self.name}: {self.uint2decimal(balance)}'
        

