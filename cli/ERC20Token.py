from web3 import Web3
from dotenv import load_dotenv
import os
import json
import sys
import time
import requests

load_dotenv()

POLLING_INTERVAL_SECONDS = int(os.getenv("POLLING_INTERVAL_SECONDS", default=5))
ETHPLORER_API_KEY = os.getenv("ETHPLORER_API_KEY", default="freekey")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
ETHERSCAN_URL = "https://api.etherscan.io/api"

w3 = Web3(Web3.HTTPProvider(os.getenv("HTTPS_RPC_URL")))

with open('abi.json') as abi:
    ERC20_ABI = json.load(abi)

# This Class is not fully ERC20 Token defined
# This class contains only Read Function due to cost for Write Functin Cost Checking

class ERC20Contract:
    def __init__(self, addr):
        self.address = Web3.toChecksumAddress(addr)
        #0xb8c77482e45F1F44dE1745F52C74426C631bDD52
        #0xB8c77482e45F1F44dE1745F52C74426C631bDD52
        if not Web3.isAddress(self.address):
            sys.stderr.write('Invalid Contract Address\n')
            sys.exit(2)

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
        else:
            decimal = value
            for i in range(self.decimals):
                decimal /= 10.0

        return decimal

    def balanceOf(self, addr):
        if not Web3.isAddress(addr):
            sys.stderr.write('Invalid Tartget Address\n')
            sys.exit(2)
        balance = self.contract.functions.balanceOf(addr).call()
        return f'Balance of {self.name}: {self.uint2decimal(balance)}'

    def subscribe_tx(self):
        event_filter = w3.eth.filter({
            'fromBlock':'latest', 
            'address':self.address
        })

        while True:
            tx_set = set()
            for event in event_filter.get_new_entries():
                tx_hash = event["transactionHash"].hex()

                #PREVENT LOGGIN DUPLICATED TRANSACTIONS
                if tx_hash not in tx_set:
                    print(f'https://etherscan.io/tx/{tx_hash}')

                tx_set.add(event["transactionHash"].hex())
            try:
                time.sleep(POLLING_INTERVAL_SECONDS)
            except KeyboardInterrupt:
                sys.exit(0)
    
    def get_latest_tx(self, n):
        params = {
            "module": "account",
            "action": "txlist",
            "address": self.address,
            "page": 1,
            "offset": n,
            "sort": "desc",
            "apikey": ETHERSCAN_API_KEY
        }
        resp = requests.get(ETHERSCAN_URL, params=params)
        txn_details = []
        for txn in resp.json()['result']:
            tx_hash = txn["hash"]
            sender = txn["from"]
            try:
                calldata = self.contract.decode_function_input(txn["input"])
            except:
                calldata = f"Could not decode calldata. For more detail please check at https://etherscan.io/tx/{tx_hash}"
            txn_details.append({
                "tx_hash": tx_hash,
                "sender": sender,
                "calldata": calldata
            })
        return txn_details
    
    def fetch_transfer_event(self, page=1, startblock=0):
        params = {
            "module": "account",
            "action": "tokentx",
            "contractaddress": self.address,
            "page": 1,
            "offset": 10000,
            "startblock": startblock,
            "sort": "asc",
            "apikey": ETHERSCAN_API_KEY
        }
        resp = requests.get(ETHERSCAN_URL, params=params)
        return resp.json()['result']

    def get_top_holders(self, n):
        # params = {
        #     "apiKey": ETHPLORER_API_KEY,
        #     "limit": n
        # }
        # url = f'https://api.ethplorer.io/getTopTokenHolders/{self.address}'
        # resp = requests.get(url, params=params).json()
        # return resp

        print(self.fetch_transfer_event())
        pass
        

