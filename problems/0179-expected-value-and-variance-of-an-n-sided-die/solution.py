def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	sum = 0
	for i in range(n + 1):
		sum += i 
	e = sum / n
	var = ((n +1) * (2* n + 1)/ 6) - e ** 2
	return e, var