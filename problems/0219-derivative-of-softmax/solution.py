import numpy as np
def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	# Your code here
	n = len(x)
	x = np.asarray(x)
	J = np.zeros((n, n))
	x = np.exp(x) / np.sum(np.exp(x))
	for i in range(n):
		for j in range(n):
			if i == j:
				J[i][j] = x[i] * (1 - x[i])
			else:
				J[i][j] = -x[i] * x[j]
	return J