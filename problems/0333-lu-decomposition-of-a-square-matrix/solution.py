import numpy as np

def lu_decomposition(A: list) -> tuple:
	"""
	Perform LU decomposition on a square matrix using Doolittle's method.
	
	Args:
		A: Square matrix as a list of lists
	
	Returns:
		tuple: (L, U) where L is lower triangular with 1s on diagonal,
		       U is upper triangular, and A = L @ U
	"""
	# Your code here
	A = np.array(A, dtype=float)
	n = len(A)
	L = np.zeros((n, n))
	U = np.zeros((n, n))
	for i in range(n):
		L[i][i] =  1.0
	for i in range(n):
		for j in range(i, n):
			tmp = 0.0
			for k in range(i):
				tmp += L[i][k] * U[k][j]
			U[i][j] = A[i][j] - tmp 
		for j in range(i + 1, n):
			tmp = 0.0
			for k in range(i):
        		tmp += L[j][k] * U[k][i]
			if U[i][i] == 0:
				raise ZeroDivisionError("division 0")
			L[j][i] = (1 / U[i][i]) * (A[j][i] - tmp)
	return (L, U)