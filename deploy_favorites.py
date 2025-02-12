import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account


load_dotenv()
def main():
    #Setting envorinment (rpc wich is the node to interact with the blockchain)
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    # Setting the key to sign transactions, remember to use encrypted keys (don't use .env files)
    # for the sake of simplicity we added the Anvil key to .env (don't do it with real keys)
    key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(key)
    boa.env.add_account(my_account, force_eoa=True)
    #this compiles and deploys the contract
    favorites_contract = boa.load("favorites.vy")

    init_favorite_number = favorites_contract.retrieve() #this is the retrieve function from the contract
    print(f"Initial favorite number is: {init_favorite_number}")
    favorites_contract.store(100) # this is the store function from the contract
    updated_favorite_number = favorites_contract.retrieve()
    print(f"Updated favorite number is: {updated_favorite_number}")

if __name__ == "__main__":
    main()

