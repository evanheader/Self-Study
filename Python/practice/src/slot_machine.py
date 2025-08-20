# Python Slot Machine
import random
import time

def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]
    
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 20
        elif row[0] == '🍉':
            return bet * 20
        elif row[0] == '🍋':
            return bet * 20
        elif row[0] == '🔔':
            return bet * 25
        elif row[0] == '⭐':
            return bet * 30
    else:
        return 0

def main():
    balance = 100
    
    print("*************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")
    
    while balance > 0:
        print(f"Current Balance: ${balance}")
        
        bet = input("Place Your Bet Amount: ")
        
        while not bet.isdigit():
            bet = input("Try again: ")
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficent Funds")
            continue
    
        if bet <= 0:
            print("Invalid Amount")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spinning...")
        time.sleep(.5)
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout == 0:
            print("You lose")
        else:
            print(f"You won ${payout}")
            balance += payout
        print()
        
        play_again = input("Do you want to spin again?: ")
        
        if play_again.upper() != 'Y':
            break

    print()
    print(f"Game Over! Final Balance: ${balance}")
    
if __name__ == "__main__":
    main()