import web3

def get_detail(args):
    addr = args.detail[0]
    mock_detail = {
        "name": "BOOM",
        "symbol": "BM",
        "decimals": 18
    }
    print(mock_detail)
    return