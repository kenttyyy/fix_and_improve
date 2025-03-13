# Explain program
print("This program checks if a number is unique or duplicate.")

def check_duplicate():
    nums = []  # List to store entered numbers.

    while True:
        try:
            num = int(input("Enter a number: "))

# If the number is already in the list, print "Duplicate".
            if num in nums:
                print("Duplicate")
            else:
# If the number is new, print "Unique" and add it to the list.
                print("Unique")
                nums.append(num)

# If the user enters a non-numeric value, exit the loop.
        except ValueError:
            print("Invalid input. Exiting.")
            break

# Call the function to execute the program.
check_duplicate()