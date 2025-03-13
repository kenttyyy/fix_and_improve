# Ask user input
try:
    num_1 = float(input("Please input the first number: "))
    num_2 = float(input("Please input the second number: "))

# Calculates the division,
    if num_2 == 0:
        print("Division by zero is not allowed")
    else:
        print(f"The quotient is: {num_1 / num_2}")\

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")