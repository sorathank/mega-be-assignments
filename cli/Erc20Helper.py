import argparse

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
    arg_parser.add_argument(
        "--balanceOf", 
        type = str, 
        nargs = 2,
        metavar = ("<contract_address>", "<target_address>"),
        default = None,
        help = "Get amount of ERC20 Token <contract_address> belong to <target_address>"
        )
    arg_parser.add_argument(
        "--watch_tx", 
        type = str, 
        nargs = 1,
        metavar = "<contract_address>",
        default = None,
        help = "Subscribe Tx from <contract_address> and keep logging URL to etherscan.io"
        )
    arg_parser.add_argument(
        "--latest_tx", 
        type = str, 
        nargs = 2,
        metavar = ("<N>", "<contract_address>"),
        default = None,
        help = "Generate Latest N (1 <= N <= 100) transaction into a text file contains TxHash, Sender Address, Decoded Call Data"
        )
    arg_parser.add_argument(
        "--holders", 
        type = str, 
        nargs = 2,
        metavar = ("<N>", "<contract_address>"),
        default = None,
        help = "Generate Top N Holders (1 <= N <= 100) into a text file contains Holder Addresses and Balances"
        )

    args = arg_parser.parse_args()
    if args.detail != None: 
        get_detail(args)
    else:
        print("NOT IMPLEMENTED")

if __name__ == "__main__":
    main()