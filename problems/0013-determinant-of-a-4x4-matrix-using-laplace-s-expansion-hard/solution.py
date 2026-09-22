def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	n = len(matrix)
	def det_2D(matr):
		size = len(matr)
		if size == 1:
			return matr[0][0]
		if size == 2:
			return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
		det = 0
		for j in range(size):
			mat = [[row[col] for col in range(size) if col != j]
					for row_idx, row in enumerate(matr) if row_idx != 0]
			det += ((-1) ** j) * matr[0][j] * det_2D(mat)
		return det
	det =  det_2D(matrix)
	return det