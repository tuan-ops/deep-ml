import numpy as np

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	if len(list(point)) == 3:
		x, y, z = point
	else:
		x, y = point
	if func_name == 'poly2d':
		return (2 * x * y + y * y, 2 * x * y + x * x)
	elif func_name == 'exp_sum':
		return (np.exp(x + y), np.exp(x + y))
	elif func_name == 'product_sin':
		return (np.sin(y), x * np.cos(y))
	elif func_name == 'poly3d':
		return (2 * x * y, x*x + z * z, 2 * y * z)
	elif func_name == 'squared_error':
		return (2 * (x-y), -2*(x-y))
	