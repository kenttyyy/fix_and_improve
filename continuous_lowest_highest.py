# Explain the program
print("This program sorts numbers from lowest to highest.")

def sort_numbers():
    nums = []  # List to store the entered numbers.

    while True:  # Infinite loop to continuously ask for input.
        try:
            nums.append(int(input("Enter a number: ")))  # Add user input to the list.

# If the user enters a non-numeric value, exit the loop.
        except ValueError:
# Check if numbers were entered before sorting and displaying them.
            if nums:
                print("Sorted numbers:", sorted(nums))  # Print sorted numbers.
            else:
                print("No numbers entered.")  # Message if no input was given.
            break  # Exit the loop.

# Call the function to execute the program.
sort_numbers()