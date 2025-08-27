# Welcome message
print("Welcome. With this program, you can calculate the factorial of a positive integer.\n")

# Get user input and convert to integer
x = int(input("Please enter a positive integer: "))

factorial = 1

# Check if the number is negative
if x < 0:
    print("Invalid number")
# Check if the number is 0 or 1 (factorial is 1)
elif x == 0 or x == 1:
    print(f'The factorial of {x} is 1')
else:
    # Calculate factorial for numbers greater than 1
    for i in range(1, x + 1):
        factorial = factorial * i
    print(f'The factorial of {x} is {factorial}')

