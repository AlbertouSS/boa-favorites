import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
import os
from eth_account import Account

load_dotenv()
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

def main():
    rpc = os.getenv("RPC_URL")
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)
    
    key = os.getenv("ANVIL_KEY")
    my_account = Account.from_key(key)
    boa.env.add_account(my_account, force_eoa=True)
    
    # loads the contract which was already deployed using the load() function
    favorite_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorite_deployer.at(CONTRACT_ADDRESS)

    favorites_contract.store(200)
    favorite_number = favorites_contract.retrieve()
    print(favorite_number)


if __name__ == "__main__":
    main()