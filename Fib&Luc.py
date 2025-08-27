# Welcome message and instructions
print("Welcome. Using this program, you can find the nth Fibonacci and Lucas numbers.\n")

# Get the term number from the user
term_number = int(input('Enter the term number (n) for the Fibonacci and Lucas sequences: '))

# Calculate the golden ratio and its conjugate
golden_ratio = (1 + 5 ** 0.5) / 2
conjugate = (1 - 5 ** 0.5) / 2

# Use Binet's formula to calculate the nth Fibonacci number
fibonacci_n = (golden_ratio ** term_number - conjugate ** term_number) / (5 ** 0.5)

# Use Binet's formula to calculate the nth Lucas number
lucas_n = (golden_ratio ** term_number + conjugate ** term_number)

# Display the results
print(f"F{term_number} (Fibonacci) is {fibonacci_n} and L{term_number} (Lucas) is {lucas_n}")
