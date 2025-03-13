# Explains what the program do
print("This program calculates the result of raising the first number to the power of the second number.")

# Ask to input two numbers
try:
    num_1 = float(input("Please input the base number: "))
    num_2 = float(input("Please input the exponent: "))

# Do the necessary calculation when raised
    print(f"The result is: {num_1 ** num_2}")

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")