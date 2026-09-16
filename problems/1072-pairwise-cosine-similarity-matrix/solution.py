import numpy as np

def pairwise_cosine_similarity(X):
    """
        Đo góc giữa hai vector thay vì là đo khoảng cách trong không gian nhiều 
    """
    norm = np.linalg.norm(X, axis = 1, keepdims= True)
    norm = np.where(norm == 0, 1e-12, norm)
    X_norm = X / norm
    return np.dot(X_norm, X_norm.T)