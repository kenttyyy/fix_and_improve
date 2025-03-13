# Explain the program
print("This program shows numbers that don’t have duplicates.")

def unique_numbers():
# Ask the user to input 10 numbers and store them in a list.
    nums = [int(input("Enter a number: ")) for _ in range(10)]

# Create a new list containing only the numbers that appear once.
    uniques = [n for n in nums if nums.count(n) == 1]