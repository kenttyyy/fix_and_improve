# Explain the program
print("This program prints all numbers between two given numbers.")

# Prompt to input
try:
    num_1 = int(input("Please input the first number: "))
    num_2 = int(input("Please input the second number: "))

# Swap to ensure correct order
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1

    for i in range(num_1 + 1, num_2):
        print(i)

except ValueError:
    print("Please input a valid integer")

print("Thanks for using the program!")