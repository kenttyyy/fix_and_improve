# Explain the program
print("This program finds the number with the most duplicates from your inputs.")

# Dictionary to store number occurrences
numbers = {}

# Increment count of entered number
try:
    while True:
        num = int(input("Enter a number: "))
        numbers[num] = numbers.get(num, 0) + 1

except ValueError:
    if numbers:
        # Find the number with the highest count using max()
        most_frequent = max(numbers, key=numbers.get)
        print(f"The number with the most duplicates is: {most_frequent}")
    else:
        print("No numbers were entered.")

print("Thanks for using the program!")