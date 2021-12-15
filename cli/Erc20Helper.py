from Parser import CustomParser
from middleware import *
import sys

def main():
    arg_parser = CustomParser(description="ERC20 Helper")

    arg_parser.add_argument(
        "-d",
        "--detail", 
        type = str, 
        nargs = 1,
        metavar = "<CONTRACT_ADDRESS>",
        default = None,
        help = "Get Token's name, symbol and decimals from Contract Address"
        )
    arg_parser.add_argument(
        "-b",
        "--balanceOf", 
        type = str, 
        nargs = 2,
        metavar = ("<CONTRACT_ADDRESS>", "<TARGET_ADDRESS>"),
        default = None,
        help = "Get Amount of ERC20 Token <CONTRACT_ADDRESS> belong to <target_address>"
        )
    arg_parser.add_argument(
        "-w",
        "--watch_tx", 
        type = str, 
        nargs = 1,
        metavar = "<CONTRACT_ADDRESS>",
        default = None,
        help = "Subscribe Tx from <CONTRACT_ADDRESS> and keep logging URL to etherscan.io"
        )
    arg_parser.add_argument(
        "-l",
        "--latest_tx", 
        type = str, 
        nargs = 2,
        metavar = ("<N>", "<CONTRACT_ADDRESS>"),
        default = None,
        help = "Generate Latest N (1 <= N <= 100) transaction into a text file contains TxHash, Sender Address, Decoded Call Data"
        )
    arg_parser.add_argument(
        "--holders", 
        type = str, 
        nargs = 2,
        metavar = ("<N>", "<CONTRACT_ADDRESS>"),
        default = None,
        help = "Generate Top N Holders (1 <= N <= 100) into a text file contains Holder Addresses and Balances"
        )

    if len(sys.argv) == 1:
        sys.stderr.write('error: no argument given\n')
        arg_parser.print_help()
        sys.exit(2)

    args = arg_parser.parse_args()
    if args.detail != None: 
        get_detail(args.detail[0])
    elif args.balanceOf != None:
        get_balanceOf(args.balanceOf[0], args.balanceOf[1])
    elif args.watch_tx != None:
        subscribe_tx(args.watch_tx[0])
    elif args.latest_tx != None:
        get_latest_tx(args.latest_tx[0], args.latest_tx[1])
    elif args.holders != None:
        get_top_holders(args.holders[0], args.holders[1])

if __name__ == "__main__":
    main()