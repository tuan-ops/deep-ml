
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	m = len(v)
	up = 0
	for i in range(m):
		up += v[i] * L[i]
	do = 0
	for i in range(m):
		do += L[i] * L[i]
	x = up / do
	for i in range(m):
		L[i] *= x
	return L
