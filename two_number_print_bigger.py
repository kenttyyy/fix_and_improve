# Create the variable for the numbers and input for the user

try:
    num_one = int(input("Please enter the first number "))
    num_two = int(input("Please enter the second number "))

# Main part of the program
    if num_one > num_two:
        print(f"{num_one}")
    elif num_one < num_two:
        print(f"{num_two}")
    else:
        print(f"{num_one} and {num_two} are equal")

# Added as a means of verifying an invalid input
except ValueError:
    print("Please input a whole number")



