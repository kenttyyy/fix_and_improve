# Tell how the program works
print("This program counts how many odd numbers are entered.")

# Set the total count to zero
count = 0

# Prompts the user to enter 10 numbers
try:
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        if num % 2 != 0:
            count += 1

# Shows the odd numberss
    print(f"Total odd numbers: {count}")

except ValueError:
    print("Please input a valid integer")

print("Thanks for using the program!")