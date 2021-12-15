from web3 import Web3, contract
from dotenv import load_dotenv
import os
import json
import sys
import time

load_dotenv()

EVENT_POLLING_INTERVAL=5 #SECONDS
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
        self.address = Web3.toChecksumAddress(addr)

        try:
            self.contract = w3.eth.contract(address=self.address, abi=ERC20_ABI)
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

    def subscribe_tx(self):
        event_filter = w3.eth.filter({'fromBlock':'latest', 'address':self.address})
        while True:
            tx_set = set()
            for event in event_filter.get_new_entries():
                tx_hash = event["transactionHash"].hex()
                if tx_hash not in tx_set:
                    print(f'https://etherscan.io/tx/{tx_hash}')
                tx_set.add(event["transactionHash"].hex())
            time.sleep(EVENT_POLLING_INTERVAL)
    
    def get_latest_tx(self, n):
        pass
        

