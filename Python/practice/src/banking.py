# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: $"))
    
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: $"))
    
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Funds")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        while choice not in ["1", "2", "3", "4"]:
            choice = input("Try again: ")
        
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        print()
                
    print("Thank you have a nice day!")
    
if __name__ == "__main__":
    main()