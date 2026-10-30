# --- cell 1 ---
import numpy as np

def train(X, y, W, b):
    """
    Train linear regression weights on standardized data.
    
    Args:
        X: numpy array of shape (n_samples, n_features) -- standardized features
        y: numpy array of shape (n_samples,) -- standardized targets
        W: numpy array of shape (n_features,) -- initial random weights
        b: float -- initial bias (0.0)
    
    Returns:
        W: numpy array of shape (n_features,) -- trained weights
        b: float -- trained bias
    """
    # TODO: implement your training strategy here
    # You can use ANY approach: gradient descent, normal equation,
    # momentum, adaptive learning rates, mini-batching, etc.
    X = np.asarray(X)
    y = np.asarray(y)
    W = np.asarray(W)
    b = np.asarray(b)
    W = np.linalg.pinv(X.T @ X) @ (X.T @ y)
    b = float(np.mean(y) - np.mean(X, axis=0) @ W)
    return W, b