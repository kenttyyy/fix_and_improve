# Explain program
print("\nThis program finds the lowest number entered.")

def find_lowest():
    nums = []  # List to store the entered numbers.

    while True:  # Infinite loop to continuously ask for input.
        try:
            nums.append(int(input("Enter a number: ")))  # Add user input to the list.

# If the user enters a non-numeric value, exit the loop.
        except ValueError:
# Check if numbers were entered before displaying the lowest one.
            if nums:
                print("Lowest number:", min(nums))  # Print the smallest number.
            else:
                print("No numbers entered.")  # Message if no input was given.
            break  # Exit the loop.

# Call the function to execute the program.
find_lowest()