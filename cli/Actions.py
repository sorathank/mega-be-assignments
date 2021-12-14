import web3

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