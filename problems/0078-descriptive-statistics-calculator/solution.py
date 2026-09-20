import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    n = len(data)
    mean  = np.mean(data)
    median = np.median(data)
    val, cnt = np.unique(data, return_counts = True)
    mode = val[np.argmax(cnt)]
    variance = 1/ n * ((np.sum((data - mean) * (data - mean))))
    standard_deviation = np.sqrt(variance)
    th_percentile_25 = np.percentile(data, 25)
    th_percentile_50 = median
    th_percentile_75 = np.percentile(data,75)
    interquartile_range = th_percentile_75 - th_percentile_25
    return {'mean': mean, 'median': median, 'mode': mode, 'variance': variance, 'standard_deviation': standard_deviation, '25th_percentile': th_percentile_25, '50th_percentile': th_percentile_50, '75th_percentile': th_percentile_75, 'interquartile_range': interquartile_range}
