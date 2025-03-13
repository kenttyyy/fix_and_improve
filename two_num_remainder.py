# Explain program
print("This program calculates the remainder when the first number is divided by the second number.")

# Enter two numbers
try:
    num_1 = int(input("Please input the first number: "))
    num_2 = int(input("Please input the second number: "))

# Divides and get the remainder
    if num_2 == 0:
        print("Division by zero is not allowed")
    else:
        print(f"The remainder is: {num_1 % num_2}")

except ValueError:
    print("Please input a valid integer")

print("Thanks for using the program!")