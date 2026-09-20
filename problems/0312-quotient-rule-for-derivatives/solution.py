import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    n = len(g_coeffs) - 1
    g_gradi = 0
    g, h = 0.0 ,0.0
    for i in g_coeffs:
        if n <= 0: break
        g_gradi += i * (n) * (x ** (n - 1)) 
        g += i * (x ** (n))
        n -= 1
    g += g_coeffs[-1]
    m = len(h_coeffs) - 1
    h_gradi = 0
    for i in h_coeffs:
        if m <= 0: break
        h_gradi += i * (m) * (x ** (m - 1))
        h += i * (x ** m)
        m -= 1
    h += h_coeffs[-1]
    if h * h == 0.0: return -1.0
    f_gradi = (g_gradi * h - h_gradi * g) / (h * h)
    return f_gradi