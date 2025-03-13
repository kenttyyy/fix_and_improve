# Explain the program
print("This program sorts all entered numbers from highest to lowest.")

# List to store input numbers
numbers = []

# Prompt to enter a number
try:
    while True:
        numbers.append(int(input("Enter a number: ")))
except ValueError:
    if numbers:
        # Sort numbers in descending order
        numbers.sort(reverse=True)
        print("Numbers from highest to lowest:", ", ".join(map(str, numbers)))
    else:
        print("No numbers were entered.")

print("Thanks for using the program!")