import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	functions = np.asarray(functions)
	res = 1.0
	curr = x
	for func in reversed(functions):
		if func == 'square':
			res *= 2 * curr
			curr = curr ** 2
		elif func == 'sin':
			res *= np.cos(curr)
			curr = np.sin(curr)
		elif func == 'exp':
			res *= np.exp(curr)
			curr = np.exp(curr)
		elif func == 'log':
			res *= 1/curr
			curr = np.log(curr)
	return res