from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

web3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))

# print(web3.isConnected())

def get_detail(contract_addr):
    mock_detail = {
        "name": "BOOM",
        "symbol": "BM",
        "decimals": 18
    }
    print(mock_detail)
    return

def get_balanceOf(contract_addr, target_addr):
    print(f"balanceOf {contract_addr}, {target_addr}")
    return

def subscribe_tx(contract_addr):
    print(f"subscribe {contract_addr}")
    return

def get_latest_tx(n, contract_addr):
    print(f"get {n} latest tx of {contract_addr}")
    return

def get_top_holders(n, contract_addr):
    print(f"get {n} top holders of {contract_addr}")
    return