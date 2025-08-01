# This is my first Python program
# only covering topics I didn't remember syntax for

import math

# Variables
first_name = "Evan"
last_name = "Hollingshead"
age = 21

# Printing
print("-------------------------")
print("I like ceviche!")
print(f"My name is {first_name} I am {age} years old")


# Type Casting
print("-------------------------")
print("Type Casting Example")
print("Before:")
print(f"the type of variable age is: {type(age)}\n")

age = float(age)
print("After:")
print(f"the type of variable age is: {type(age)}")

# Input
print("-------------------------")
print("Input Example")

user_name = input("What is your name?: ")
print()
print(f"Hello {user_name}")

# Arithmetic
x = 5
y = 25
round(x)
abs(x)
pow(x,2)
max(x,y)
min(x,y)
math.pi
math.sqrt(y)
math.ceil(x)
math.floor(x)

# If Statements

user_age = int(input("What is your age?: "))
if user_age >= 21:
    print("You are old enough")
elif user_age >= 18:
    print("Almost there")
else:
    print("You are too young")