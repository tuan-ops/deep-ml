def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	# Your code here
	n = len(matrix)
	trace = 0
	for i in range(n):
		trace += matrix[i][i]
	def det_2D(matr):
		size = len(matr)
		if size == 1:
			return matr[0][0]
		if size == 2:
			return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
		det = 0
		for j in range(size):
			mat = [[row[col] for col in range(n) if col != j]
					for row_idx, row in enumerate(matrix) if row_idx != 0]
			det += ((-1) ** j) * matrix[0][j] * det_2D(mat)
		return det
	det =  det_2D(matrix)
	return (det, trace)

			