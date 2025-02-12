import boa

def main():
    #this compiles and deploys the contract
    favorites_contract =  boa.load("favorites.vy")
    # print(favorites_contract)

    init_favorite_number = favorites_contract.retrieve() #this is the retrieve function from the contract
    print(f"Initial favorite number is: {init_favorite_number}")

    favorites_contract.store(100) # this is the store function from the contract
    updated_favorite_number = favorites_contract.retrieve()
    print(f"Updated favorite number is: {updated_favorite_number}")

if __name__ == "__main__":
    main()
