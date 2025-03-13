# Explain program
print("This program calculates the result of subtracting all numbers from the first number.")

# Enter the first number
try:
    num_1 = float(input("Please input the first number: "))
    total = num_1

# Ten numbers that will be used
    for i in range(9):
        num = float(input(f"Enter number {i + 2}: "))
        total -= num

# Remaining after subtraction
    print(f"Result after subtraction: {total}")

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")