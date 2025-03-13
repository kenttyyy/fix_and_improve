# Ask the user to input two number
try:
    num_one = float(input("Input the first number "))
    num_two = float(input("Input the second number "))

# Checks if the number is equal
    if num_one == num_two:
        print("Equal")

except ValueError:
    print("Please enter a whole number")
 