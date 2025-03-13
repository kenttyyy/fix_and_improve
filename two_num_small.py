# Explain the program
print("This program prints the smaller number based on the input of the user.")

# Prompt to input two numbers
try:
    num_1 = float(input("Please input the first number: "))
    num_2 = float(input("Please input the second number: "))

# Checks the smaller number then print
    if num_1 < num_2:
        print(f"{num_1} is smaller")
    elif num_1 > num_2:
        print(f"{num_2} is smaller")
    else:
        print("Both numbers are equal")

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")