import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a = np.asarray(a)
	x, y = a.shape
	if x not in new_shape or y not in new_shape :
		return []
	a.reshape((new_shape))
	return a