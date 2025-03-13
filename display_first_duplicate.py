# Explain program
print("This program shows numbers, but duplicates appear only once.")

def first_occurrences():
    nums = []  # List to store the unique numbers.
    seen = set()  # Set to track numbers that have been seen before.

# Loop to get 10 numbers from the user.
    for _ in range(10):  # Loop to get 10 numbers from the user.
        while True:
            try:
                num = int(input("Enter a number: "))
# If input is valid, exit the loop.
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

# If the number is not in the set, add it.
        if num not in seen:
            nums.append(num)
            seen.add(num)

# Display the numbers.
    print("Numbers:", nums)

# Call the function to run the program
first_occurrences()