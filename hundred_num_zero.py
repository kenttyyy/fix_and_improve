# Explain program
print("This program prints numbers from 0 to 100 except those ending in zero or five.")

# Exclude zero and five
for i in range(101):
    if i % 10 != 0 and i % 10 != 5:
        print(i)

print("Thanks for using the program!")