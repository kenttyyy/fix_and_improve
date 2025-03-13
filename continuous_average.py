# Explain the program
print("This program calculates the average of entered numbers.")

# List to store input numbers
numbers = []

try:
    while True:
        numbers.append(float(input("Enter a number: ")))

except ValueError:
    if numbers:
# Calculate the average by dividing the sum by the count
        average = sum(numbers) / len(numbers)
        print(f"The average of the numbers entered is: {average:.2f}")
    else:
        print("No numbers were entered.")

print("Thanks for using the program!")