# Explain how program works
print("This program displays all numbers that have duplicates among the 10 inputs.")

# Store the 10 numbers in a list
numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# Find numbers that appear more than once using a set comprehension
duplicates = set(num for num in numbers if numbers.count(num) > 1)
