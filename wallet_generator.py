# wallet_generator.py
from algosdk import account

# Generate a new Algorand account
private_key, address = account.generate_account()

print("Algorand Address:", address)
print("Private Key:", private_key)
