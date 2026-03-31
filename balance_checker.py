# balance_checker.py
from algosdk.v2client import algod

# Connect to Algorand TestNet (public node)
algod_address = "https://testnet-api.algonode.cloud"
algod_client = algod.AlgodClient("", algod_address)

# Replace with your generated address
address = "4BY1YJDDH554KJ556QFIAO722JQA7HXGNBABISTGGW50E7QNR7KPPURA"




# Fetch account info
account_info = algod_client.account_info(address)
print("Account balance: {} microAlgos".format(account_info.get('amount')))
