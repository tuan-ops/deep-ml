import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	x = np.asarray(x, dtype=float)
	fx = np.array(f(x))
	m = len(x)
	n = len(fx)
	J = np.zeros((n, m))
	for i in range(m):
		x_h = x.copy()
		x_h[i] += h 
		f_xh = np.array(f(x_h))
		J[:, i] = (f_xh - fx) / h 
	return J

	
