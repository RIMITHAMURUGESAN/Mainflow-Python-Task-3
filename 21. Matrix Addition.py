def add_matrices(mat1, mat2):
    rows, cols = len(mat1), len(mat1[0])
    result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Input matrices
mat1 = [[int(x) for x in input("Enter row for matrix 1: ").split()] for _ in range(2)]
mat2 = [[int(x) for x in input("Enter row for matrix 2: ").split()] for _ in range(2)]

# Matrix addition
sum_matrix = add_matrices(mat1, mat2)

# Print result
print("Sum of matrices:")
for row in sum_matrix:
    print(row)