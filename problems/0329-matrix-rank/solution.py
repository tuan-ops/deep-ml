import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    m, n = len(A), len(A[0])
    col = 0
    rank = 0
    matrix = [[float(val) for val in row] for row in A]
    for i in range(m):
        if col >= n:
            break
        max_row = i
        for row in range(i + 1, m):
            if abs(matrix[row][col] )>=abs( matrix[max_row][col]):
                max_row = row 
        while col < n and abs(matrix[max_row][col]) < tol:
            col += 1
            if col < n:
                for row in range(i + 1, m):
                    if abs(matrix[row][col]) >= abs(matrix[max_row][col]):
                        max_row = row
        if col >= n:
            break
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        for row in range(i + 1, m):
            factor = matrix[row][col] / matrix[i][col]
            for j in range(n):
                matrix[row][j] -= factor * matrix[i][j]
        rank += 1
        col += 1
    return rank
