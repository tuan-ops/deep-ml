import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    N = len(y)
    m = len(batch_indices)
    Xi = []
    yi = []
    y_pred = []
    for batch in batch_indices:
        y_pred.append(X[batch] @ weights + bias)
        Xi.append(X[batch])
        yi.append(y[batch])
    y_pred = np.array(y_pred)
    yi = np.array(yi)
    Xi = np.array(Xi)
    error = y_pred - yi
    d_w = (2/m) * np.dot(Xi.T, error)
    d_b = 2/m * np.sum(error)
    weights -= lr * d_w 
    bias -= lr * d_b
    result = list(weights)
    result.append(bias)
    return result
