# Shopping cart program
# Practice for collections

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food you'd like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the value of {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("--- Your Cart ---")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
    
print()
print(f"Your total is: ${total:.2f}")