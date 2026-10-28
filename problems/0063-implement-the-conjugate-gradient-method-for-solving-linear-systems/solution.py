import numpy as np

def conjugate_gradient(A, b, n, x0=None, tol=1e-8):
	"""
	Solve the system Ax = b using the Conjugate Gradient method.

	:param A: Symmetric positive-definite matrix
	:param b: Right-hand side vector
	:param n: Maximum number of iterations
	:param x0: Initial guess for solution (default is zero vector)
	:param tol: Convergence tolerance
	:return: Solution vector x
	"""
	# calculate initial residual vector
	m = len(b)
	if x0 is None:
		x = np.zeros(m)
	else:
		x = x0.copy()
	r = b - A @ x
	d = r.copy()
	rs_old = np.dot(r, r)
	for k in range(n):
		if np.sqrt(rs_old) < tol:
			return x
		Ad = np.dot(A, d)
		alpha_k = rs_old / np.dot(d, Ad)
		r = r - alpha_k * Ad
		x = x + alpha_k * d 
		rs_new = np.dot(r, r)
		beta_k = rs_new / rs_old
		d = r + beta_k * d
		rs_old = rs_new
	return x
