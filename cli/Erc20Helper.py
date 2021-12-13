import argparse

def get_detail(args):
    addr = args.detail[0]
    mock_detail = {
        "name": "BOOM",
        "symbol": "BM",
        "decimals": 18
    }
    print(mock_detail)
    return

def main():
    arg_parser = argparse.ArgumentParser(description="TEST ARG_PARSER")
    arg_parser.add_argument(
        "--detail", 
        type = str, 
        nargs = 1,
        metavar = "<contract_address>",
        default = None,
        help = "Get Token's name, symbol and decimals from Contract Address"
        )
    args = arg_parser.parse_args()

    if args.detail != None: 
        get_detail(args)
    else:
        "NOT IMPLEMENTED"

if __name__ == "__main__":
    main()