# Explain how the program works
print("This program calculates the sum of 10 numbers.")

# initialize the total to zero
total = 0

# This makes the continuous enter of 10 numbers
try:
    for i in range(10):
        num = float(input(f"Enter number {i + 1}: "))
        total += num
    print(f"The total sum is: {total}")

except ValueError:
    print("Please input a valid number")

print("Thanks for using the program!")