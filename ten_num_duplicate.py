# Explain how program works
print("This program displays all numbers that have duplicates among the 10 inputs.")

# Store the 10 numbers in a list
try:
    numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# Find numbers that appear more than once using a set comprehension
    duplicates = set(num for num in numbers if numbers.count(num) > 1)

# Display the duplicate numbers if found
    if duplicates:
        print("Duplicate numbers:", ", ".join(map(str, duplicates)))
    else:
        print("No duplicates found.")

except ValueError:
    print("Please input a valid integer.")

print("Thanks for using the program!")