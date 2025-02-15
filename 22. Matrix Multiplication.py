def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Initialize result matrix with zeros
    result = [[0] * cols_B for _ in range(rows_A)]
    
    # Multiply matrices
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Input matrices
A = [[int(x) for x in input("Enter row for matrix A: ").split()] for _ in range(2)]
B = [[int(x) for x in input("Enter row for matrix B: ").split()] for _ in range(2)]

# Multiply matrices
product_matrix = multiply_matrices(A, B)

# Print result
print("Product of matrices:")
for row in product_matrix:
    print(row)