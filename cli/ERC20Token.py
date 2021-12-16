from web3 import Web3
from dotenv import load_dotenv
import os
import json
import sys
import time
import requests

load_dotenv()
RPC_URL = os.getenv("HTTPS_RPC_URL")
w3 = Web3(Web3.HTTPProvider(RPC_URL))
try:
    POLLING_INTERVAL_SECONDS = int(os.getenv("POLLING_INTERVAL_SECONDS", default=5))
except:
    sys.stderr.write('Invalid POLLING INTERVAL. Please provide integer between 1 and 1000.\n')
    sys.exit(2)  
  

ETHPLORER_API_KEY = os.getenv("ETHPLORER_API_KEY", default="freekey")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
ETHERSCAN_URL = "https://api.etherscan.io/api"
ETHPLORER_URL = "https://api.ethplorer.io"

with open('abi.json') as abi:
    ERC20_ABI = json.load(abi)

# This Class is not fully ERC20 Token defined
# This class contains only Read Function due to cost for Write Functin Cost Checking
def clean_address(addr):
    try: 
        addr = Web3.toChecksumAddress(addr)
    except:
        pass
    return addr

class ERC20Contract:
    def __init__(self, addr):
        self.address = clean_address(addr)
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
            decimal = value / 10.0**self.decimals

        return decimal

    def balanceOf(self, addr):
        if not Web3.isAddress(addr):
            sys.stderr.write('[ERROR] Invalid Tartget Address\n')
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
    
    # DEPRECATED
    def fetch_transfer_event(self, startblock=0):
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
        print(f"FETCHING -- BlockNumber {startblock}")
        resp = requests.get(ETHERSCAN_URL, params=params)
        return resp.json()['result']

    def get_top_holders(self, n):
        params = {
            "apiKey": ETHPLORER_API_KEY,
            "limit": n
        }
        url = f'{ETHPLORER_URL}/getTopTokenHolders/{self.address}'
        resp = requests.get(url, params=params).json()
        return resp
        

def env_check():
    ## .env FILE CHECK
    if not os.path.isfile('./.env'):
        sys.stderr.write('[ERROR] .env file does not exists\n')
        sys.exit(2)
    ## RPC CHECK
    if not w3.isConnected():
        sys.stderr.write('[ERROR] Please check your RPC URL\n')
        sys.exit(2)
        
    ## POLLING INTERVAL CHECK
    if POLLING_INTERVAL_SECONDS < 1 or POLLING_INTERVAL_SECONDS > 1000:
        sys.stderr.write('[ERROR] Invalid POLLING INTERVAL. Please provide integer between 1 and 1000\n')
        sys.exit(2) 
    
    ## ETHPLORER API KEY CHECK
    params = {
        "apiKey": ETHPLORER_API_KEY
    }
    resp = requests.get(f'{ETHPLORER_URL}/getLastBlock', params=params)
    if "error" in resp.json():
        sys.stderr.write('[ERROR] Invalid Ethplorer API Key\n')
        sys.exit(2)
    
    ## ETHERSCAN API KEY CHECK
    if ETHERSCAN_API_KEY == "":
        sys.stderr.write('[ERROR] Invalid Etherscan API Key\n')
        sys.exit(2)
    params = {
        'module': 'account',
        'action': 'balance',
        'address': '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        'apikey': ETHERSCAN_API_KEY,
        'tag': 'latest'
    }
    if requests.get(ETHERSCAN_URL, params=params).json()["status"] == "0":
        sys.stderr.write('[ERROR] Invalid Etherscan API Key\n')
        sys.exit(2)

    return
