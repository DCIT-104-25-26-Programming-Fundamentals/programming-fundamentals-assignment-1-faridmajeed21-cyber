# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# HELPER FUNCTIONS (Reading & Displaying)
# =============================================================================

def read_matrix(rows, cols, name="Matrix"):
    """Reads a matrix row by row from user input."""
    matrix = []
    print(f"\nEnter values for {name} ({rows}x{cols}):")
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"  Enter row {i + 1}: ").split()))
                if len(row) != cols:
                    print(f"  --> Please enter exactly {cols} space-separated integers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("  --> Invalid input! Please enter integers only.")
    return matrix


def print_matrix(matrix):
    """Prints a matrix in a neat, visually aligned grid format."""
    for row in matrix:
        formatted_row = " ".join(f"{val:>4}" for val in row)
        print(formatted_row)


# =============================================================================
# PART A — Transpose a Matrix
# =============================================================================

def transpose_matrix(matrix):
    """
    Computes the transpose of a given M x N matrix.
    Rows become columns and columns become rows (Result is N x M).
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize an N x M matrix with zeros
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Swap row and column indices using nested loops
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed


# =============================================================================
# PART B — Add Two Matrices
# =============================================================================

def add_matrices(matrix_a, matrix_b):
    """
    Computes the element-wise sum of two M x N matrices.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    # Initialize the result matrix
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Add corresponding elements using nested loops
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]
            
    return result


# =============================================================================
# PART C — Multiply Two Matrices
# =============================================================================

def multiply_matrices(matrix_a, matrix_b):
    """
    Multiplies matrix A (M x N) by matrix B (N x P).
    Result is of size M x P.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    # Initialize the result matrix of size M x P with zeros
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    # Use triple nested loops for matrix multiplication:
    # Outer two loops iterate over each cell in the result matrix.
    # The innermost loop computes the dot product of row i (from A) and col j (from B).
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][j] if False else matrix_a[i][k] * matrix_b[k][j]
                
    return result


# =============================================================================
# MAIN PROGRAM DRIVER
# =============================================================================

def main():
    print("==================================================")
    print("       PROGRAMMING FUNDAMENTALS - ASSIGNMENT 4    ")
    print("==================================================")

    # -------------------------------------------------------------------------
    # PART A DEMO: Transpose
    # -------------------------------------------------------------------------
    print("\n--- PART A: TRANSPOSE A MATRIX ---")
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    
    matrix_a = read_matrix(m, n, "Original Matrix")
    
    print("\nOriginal Matrix:")
    print_matrix(matrix_a)
    
    transposed = transpose_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # -------------------------------------------------------------------------
    # PART B DEMO: Addition
    # -------------------------------------------------------------------------
    print("\n--------------------------------------------------")
    print("--- PART B: ADD TWO MATRICES ---")
    print(f"Adding two matrices of size {m} x {n}:")
    
    matrix_b1 = read_matrix(m, n, "Matrix 1")
    matrix_b2 = read_matrix(m, n, "Matrix 2")
    
    sum_matrix = add_matrices(matrix_b1, matrix_b2)
    print("\nSum Matrix (Matrix 1 + Matrix 2):")
    print_matrix(sum_matrix)

    # -------------------------------------------------------------------------
    # PART C DEMO: Multiplication
    # -------------------------------------------------------------------------
    print("\n--------------------------------------------------")
    print("--- PART C: MULTIPLY TWO MATRICES ---")
    print("Note: Matrix A (M x N) and Matrix B (N x P)")
    
    m_c = int(input("Enter rows for Matrix A (M): "))
    n_c = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p_c = int(input("Enter columns for Matrix B (P): "))
    
    mat_a = read_matrix(m_c, n_c, "Matrix A")
    mat_b = read_matrix(n_c, p_c, "Matrix B")
    
    product_matrix = multiply_matrices(mat_a, mat_b)
    print(f"\nProduct Matrix A × B ({m_c} x {p_c}):")
    print_matrix(product_matrix)


if __name__ == "__main__":
    main()
