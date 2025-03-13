# Explain the program
print("This program finds the number with the most duplicates from your inputs.")

# Dictionary to store number occurrences
numbers = {}

# Increment count of entered number
while True:
    num = int(input("Enter a number: "))
    numbers[num] = numbers.get(num, 0) + 1