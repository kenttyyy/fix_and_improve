# Explain the program
print("This program counts how many even numbers are entered.")

# Set count to zero
count = 0

# Create a prompt for ten numbers
try:
    for i in range(10):
        num = int(input(f"Enter number {i + 1}: "))
        if num % 2 == 0:
            count += 1

# Total even
    print(f"Total even numbers: {count}")

except ValueError:
    print("Please input a valid integer")

print("Thanks for using the program!")