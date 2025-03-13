# Explain the program
print("This program finds the highest number from your inputs.")

# Variable to store the highest number
highest = None

# Prompt to enter number
while True:
    num = int(input("Enter a number: "))

# Update highest if it's the first number or if num is greater
    if highest is None or num > highest:
        highest = num