import math

# Welcome message
print('Welcome! This program will display the elements of two vectors and calculate their norms (lengths).')

# Ask the user for the dimension of the vectors
vector_size = int(input("Enter the dimension of the vectors: "))

# Create empty lists for the two vectors
first_vector = []
second_vector = []

# Get the elements of the first vector from the user
for i in range(vector_size):
    first_vector.append(int(input(f"Enter element {i+1} of the first vector: ")))

# Get the elements of the second vector from the user
for j in range(vector_size):
    second_vector.append(int(input(f"Enter element {j+1} of the second vector: ")))

# Print the vectors
print(f'The first vector is {first_vector}')
print(f'The second vector is {second_vector}')

# Calculate the sum of squares of the elements of both vectors
first_vector_sum_squares = 0
second_vector_sum_squares = 0

for element in first_vector:
    first_vector_sum_squares += math.pow(element, 2)

for element in second_vector:
    second_vector_sum_squares += math.pow(element, 2)

# Calculate the Euclidean norm (square root of the sum of squares)
first_vector_norm = math.sqrt(first_vector_sum_squares)
second_vector_norm = math.sqrt(second_vector_sum_squares)

# Print the results
print(f'The norm of the first vector is {first_vector_norm}')
print(f'The norm of the second vector is {second_vector_norm}')
