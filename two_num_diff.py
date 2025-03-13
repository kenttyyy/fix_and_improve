# Explain the programm
print("This program calculates the difference of two numbers.")

# User input
try:
    num_1 = float(input("Please input the first number: "))
    num_2 = float(input("Please input the second number: "))

    print(f"The difference is: {num_1 - num_2}")

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")