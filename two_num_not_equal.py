# Explain the program
print("This program checks if two numbers are not equal.")

# Prompt to input numbers
try:
    num_1 = float(input("Please input the first number: "))
    num_2 = float(input("Please input the second number: "))

# Checks if it is equal or not
    if num_1 != num_2:
        print("Not Equal")

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")