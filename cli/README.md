## How to run

First, please cd to cli directory and run the command below.

**Please use pip3 instead of pip if "pip" command in your laptop is used for python2.
```
pip install -r ./requirements.txt
```
Next step, copy .env.template file and paste it on the same folder. Then rename it to .env.

Example:

![](https://i.ibb.co/nwXTzTr/Screenshot-2021-12-16-215003.png)

Register an account on [Ethplorer](https://ethplorer.io/wallet/#) and create your API Key at [Ethplorer API Panel](https://ethplorer.io/wallet/#screen=api). 

Register an account on [Etherscan APIs](https://etherscan.io/apis) and create your API Key.

Then enter your HTTPS RPC URL, Polling interval for watch_tx command (in seconds), Ethplorer API Key and Etherscan API Key in your .env file.

To run the program, run ```python ./Erc20Helper.py``` or ```python3 ./Erc20Helper.py``` if your python command is using python2 with the following argument.

Optional Arguments:
```
  -h
  --help
  Description: Show help message
  
  -d <CONTRACT_ADDRESS>
  --detail <CONTRACT_ADDRESS> 
  Description: Get Token's name, symbol and decimals from Contract Address
  
  -b <CONTRACT_ADDRESS> <TARGET_ADDRESS>
  --balanceOf <CONTRACT_ADDRESS> <TARGET_ADDRESS>
  Description: Get Amount of ERC20 Token <CONTRACT_ADDRESS> belong to <TARGET_ADDRESS>
  
  -w <CONTRACT_ADDRESS>, --watch_tx <CONTRACT_ADDRESS>
  Description: Subscribe Tx from <CONTRACT_ADDRESS> and keep logging a URL to etherscan.io
  
  -l <N> <CONTRACT_ADDRESS>
  --latest_tx <N> <CONTRACT_ADDRESS>
  Description: Generate Latest N (1 <= N <= 100) transaction into a text file contains TxHash, 
  Sender Address, Decoded Call Data
  
  --holders <N> <CONTRACT_ADDRESS>
  Description: Generate Top N Holders (1 <= N <= 100) into a text file contains Holder 
  Addresses and Balances
```

At first, I was try to implement the --holders command handler to querying Transaction Data from Etherscan.io's API and then compute token holder's balances myself, but it is cost much time when running it. So I decide to get top holders data from ethplorer instead.
