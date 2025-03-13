# Explain the program
print("This program prints numbers from 0 to 100 except those ending in zero.")

# Print numbers in range excluding zero end
for i in range(101):
    if i % 10 != 0:
        print(i)

print("Thanks for using the program!")