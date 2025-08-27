import math

print("Welcome! You can use this program to calculate Permutation or Combination.\n")

# Function to calculate n factorial (n!)
def n_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

# Function to calculate (n - r) factorial ((n - r)!)
def n_r_factorial(n, r):
    product = 1
    for j in range(1, n - r + 1):
        product *= j
    return product

# Function to calculate r factorial (r!)
def r_factorial(r):
    product = 1
    for i in range(1, r + 1):
        product *= i
    return product

# Get user input for n and r
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

# Calculate permutation: P(n, r) = n! / (n - r)!
permutation = n_factorial(n) / n_r_factorial(n, r)

# Calculate combination: C(n, r) = n! / [(n - r)! * r!]
combination = n_factorial(n) / (n_r_factorial(n, r) * r_factorial(r))

# Print the results
print(f'P({n}, {r}) = {permutation}')
print(f'C({n}, {r}) = {combination}')
