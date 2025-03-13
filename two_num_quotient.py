# Explain program
print("This program calculates the quotient of two numbers without the decimal point.")

# Enter number
try:
    num_1 = int(input("Please input the first number: "))
    num_2 = int(input("Please input the second number: "))

# Perform division in two numbers
    if num_2 == 0:
        print("Division by zero is not allowed")
    else:
        print(f"The quotient is: {num_1 // num_2}")

except ValueError:
    print("Please input a valid integer")

print("Thanks for using the program!")