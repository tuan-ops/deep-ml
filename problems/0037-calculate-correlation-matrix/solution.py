import numpy as np

def calculate_correlation_matrix(X, Y=None):
	"""
	Với 2 biến X, Y dùng ý tưởng covariance xem X, Y có tăng/giảm với nhau hay không. Tuy nhiên cov phụ thuộc đơn vị nên phải chia cho độ lệch chuẩn để chuẩn hóa nằm trong khoảng [-1, 1]
	"""
	if Y is None:
		Y = X 
	else:
		Y = np.asarray(Y)
	X = np.asarray(X)
	n, m  = len(X), len(X[0])
	corr = np.zeros((m, m))
	for i in range(m):
		mean_i = 0
		for k in range(n):
			mean_i += X[k][i]
		mean_i /= n
		for j in range(m):
			mean_j = 0
			for k in range(n):
				mean_j += Y[k][j]
			mean_j /= n 
			cov = 0
			var_i = 0
			var_j = 0
			for k in range(n):
				x_i = X[k][i] - mean_i
				y_j = Y[k][j] - mean_j
				cov += x_i * y_j 
				var_i += x_i * x_i
				var_j += y_j * y_j
			corr[i][j] = cov / (np.sqrt(var_i*var_j))
	return corr.tolist()
