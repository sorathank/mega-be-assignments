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
    print(f"subscribe {contract_addr}")
    return

def get_latest_tx(n, contract_addr):
    print(f"get {n} latest tx of {contract_addr}")
    return

def get_top_holders(n, contract_addr):
    print(f"get {n} top holders of {contract_addr}")
    return