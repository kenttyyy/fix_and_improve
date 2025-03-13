# Ask the user to input two number
try:
    num_one = float(input("Please input the first number: "))
    num_two = float(input("Please input the second number: "))

# Calculates for the product
    print(f"The product is: {num_one * num_two}")

# Mostly add value error, just in case invalid
except ValueError:
    print("Please input a valid number")