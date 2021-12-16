import sys
from datetime import datetime
from ERC20Token import ERC20Contract

def get_detail(contract_addr):
    contract = ERC20Contract(contract_addr)
    print(f'Name: {contract.name}')
    print(f'Symbol: {contract.symbol}')
    print(f'Decimals: {contract.decimals}')
    return

def get_balanceOf(contract_addr, target_addr):
    contract = ERC20Contract(contract_addr)
    print(contract.balanceOf(target_addr))
    return

def subscribe_tx(contract_addr):
    contract = ERC20Contract(contract_addr)
    contract.subscribe_tx()
    return

def validate_n(n):
    try:
        n = int(n)
    except:
        sys.stderr.write('Invalid Number\n')
        sys.exit(2)

    if n <= 0 or n > 100:
        sys.stderr.write('Invalid Number\n')
        sys.exit(2)
    return n

def get_latest_tx(n, contract_addr):
    n = validate_n(n)
    contract = ERC20Contract(contract_addr)
    txn_details = contract.get_latest_tx(n)
    filename = f'Latest {n} {contract.name} Txn {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.txt'
    with open(filename, 'a') as file:
        for idx, txn in enumerate(txn_details):
            sender = txn['sender']
            hash = txn['tx_hash']
            calldata = txn['calldata']
            file.write(f'{idx + 1}.\nSender: {sender}\nTxn Hash: {hash}\nCall Data: {calldata}\n\n')
    return

def get_top_holders(n, contract_addr):
    n = validate_n(n)

    contract = ERC20Contract(contract_addr)
    resp = contract.get_top_holders(n)
    filename = f'Top {n} {contract.name} Holders {datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.txt'
    with open(filename, 'w') as file:
        for idx, holder in enumerate(resp['holders']):
            addr = holder['address']
            balance = holder['balance']
            decimal_balance = contract.uint2decimal(balance)

            file.write(f'{idx}. {addr}: {decimal_balance}\n')
    return