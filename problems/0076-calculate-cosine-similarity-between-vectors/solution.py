import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	v1 = np.asarray(v1)
	v2 = np.asarray(v2)
	tu_so = float(np.matmul(v1, v2))
	mau_so = float(np.sqrt(np.sum(v1 * v1)) * np.sqrt(np.sum(v2 * v2)))
	if mau_so == 0.0 : return 0.0
	return float(tu_so / mau_so)