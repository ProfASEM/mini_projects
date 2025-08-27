import math

# Welcome message and program description
print("Welcome! This program finds all numbers that are coprime with a given integer and calculates its Euler's totient function.\n")

# Get user input for an integer greater than 1
number = int(input("Enter an integer greater than 1: "))

coprime_numbers = []

if number <= 1:
    print("Invalid number")
else:
    # Check all numbers from 1 to (number - 1)
    for i in range(1, number):
        # If gcd is 1, numbers are coprime
        if math.gcd(i, number) == 1:
            coprime_numbers.append(i)

# Print the list of coprime numbers and Euler's totient function value
print(f"Numbers that are coprime with {number}: {coprime_numbers}")
print(f"Euler's totient function value for {number} is {len(coprime_numbers)}")

