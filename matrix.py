# Welcome message and instructions
print("Welcome. You can specify the number of columns and rows, enter the elements of the matrix, and find its transpose.\n")

# Get the number of columns and rows from the user
column_count = int(input("Enter the number of columns of the matrix: "))
row_count = int(input("Enter the number of rows of the matrix: "))

matrix = []

# Input matrix elements from the user
for i in range(1, row_count + 1):
    row = []
    for j in range(1, column_count + 1):
        element = int(input(f"Enter element a{i}{j}: "))
        row.append(element)
    matrix.append(row)

# Display the entered matrix
print("Entered matrix\n")
for row in matrix:
    print(row)

# Calculate the transpose of the matrix
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Display the transpose
print("Transpose of the matrix\n")
for row in transpose:
    print(row)