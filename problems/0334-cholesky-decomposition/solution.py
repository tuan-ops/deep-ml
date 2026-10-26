import numpy as np

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix.
    
    Args:
        A: A symmetric positive-definite matrix (2D list or numpy array)
    
    Returns:
        L: Lower triangular matrix such that A = L @ L.T as a 2D list,
           or -1 if decomposition is not possible
    """
    # Your code here
    A = np.asarray(A, dtype = float)
    n = len(A)
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(0, i + 1):
            if i == j:
                tmp = 0.0
                for k in range(i):
                    tmp += L[i][k] ** 2
                if A[i][i] - tmp < 0: return -1
                L[i][i] = np.sqrt(A[i][i] - tmp)
                break
            tmp = 0.0
            for k in range(j):
                tmp += L[i][k] * L[j][k]
            if L[j][j] == 0:
                raise ZeroDivisionError("division zero")
            L[i][j] = (A[i][j] - tmp ) / L[j][j]
    return L.tolist()
