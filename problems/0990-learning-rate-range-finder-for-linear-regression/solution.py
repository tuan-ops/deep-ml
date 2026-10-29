import numpy as np

def lr_range_finder(X, y, w0, a, b, n_steps):
    """
    Sweep learning rate from 10**a to 10**b over n_steps full-batch GD updates
    on a linear regression model (no bias). Return the list of MSE losses after
    each update.
    """
    N = len(y)
    X = np.asarray(X)  
    y = np.asarray(y)  
    w0 = np.asarray(w0) 
    
    result = []
    
    for n in range(n_steps):
        y_pred = X @ w0 
        if n_steps == 1:
            lr_k = 10 ** a
        else: 
            lr_k = 10 ** (a + (b - a) * n / (n_steps - 1)) 
        error = y_pred - y
        d_w = 2 / N * (X.T @ error)
        w0 -= lr_k * d_w 
        mse_loss = np.mean((X @ w0 - y) ** 2)
        result.append(float(mse_loss))
    return result