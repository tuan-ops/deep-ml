import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    N = len(y)
    for k in range(n_iter):
            i = k % N
            y_pred = X[i] @ weights
            error_i = y_pred - y[i]
            d_w = error_i * X[i] * 2
            weights -= learning_rate * d_w
    return weights