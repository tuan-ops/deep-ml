import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	features = np.asarray(features)
	labels = np.asarray(labels)
	initial_weights = np.asarray(initial_weights)
	m, n = len(features), len(features[0])
	mse_values = []
	for epoch in range(epochs):
		z = features @ initial_weights + initial_bias
		sig_z = 1 / (1 + np.exp(-z))
		mse = (1/m) * np.sum((sig_z - labels) ** 2)
		mse_values.append(mse)
		updated_weights = np.zeros(n)
		updated_bias = 0.0
		for i in range(m):
			common = (sig_z[i] - labels[i]) * sig_z[i] * (1 - sig_z[i])
			for j in range(n):
				updated_weights[j] += common * features[i][j]
			updated_bias += common
		updated_weights *= 2/m 
		updated_bias *= 2/m
		for j in range(n):
			initial_weights[j] = initial_weights[j] - learning_rate * updated_weights[j]
		initial_bias = initial_bias - learning_rate * updated_bias 
	updated_bias = initial_bias
	updated_weights = initial_weights
	return updated_weights, updated_bias, mse_values