# Ask user to input two numbers
try:
    num_one = float(input("Please input the first number: "))
    num_two = float(input("Please input the second number: "))

# Calculates the sum
    print(f"The sum is: {num_one + num_two}")

except ValueError:
    print("Please input a valid number")