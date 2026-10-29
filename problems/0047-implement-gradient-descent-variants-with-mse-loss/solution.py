import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    if method == 'batch':
        N = len(y)
        for epoch in range(n_epochs):
            d_weights = 2/N * ((X.T) @ (X @ weights - y))
            weights = weights - learning_rate * d_weights
        return weights
    elif method == 'stochastic':
        N = len(y)
        for epoch in range(n_epochs):
            for i in range(N):
                xi = X[i]
                yi = y[i]
                y_pred = xi @ weights
                error_i = y_pred - yi 
                d_w = error_i * xi * 2
                weights -= learning_rate * d_w 
        return weights 
    else:
        N = len(y)
        for epoch in range(n_epochs):
            for i in range(0, N, batch_size):
                xi = X[i:i+batch_size]
                yi = y[i:i+batch_size]
                y_pred = xi @ weights
                error_i = y_pred - yi 
                d_w = 2/ len(yi) *(np.dot(xi.T, error_i))
                weights -= learning_rate * d_w 
        return weights

