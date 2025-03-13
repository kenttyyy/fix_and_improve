# Explain the program
print("This program finds the highest number from your inputs.")

# Variable to store the highest number
highest = None

# Prompt to enter number
try:
    while True:
        num = int(input("Enter a number: "))

# Update highest if it's the first number or if num is greater
        if highest is None or num > highest:
            highest = num
except ValueError:
        if highest is not None:
            print(f"The highest number entered is: {highest}")
        else:
            print("No numbers were entered.")

print("Thanks for using the program!")