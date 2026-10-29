import math
import numpy as np
PI = 3.14159

def power_grid_forecast(consumption_data):
	# 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
	# 2) Perform linear regression on the detrended data.
	# 3) Predict day 15's base consumption.
	# 4) Add the day 15 fluctuation back.
	# 5) Round, then add a 5% safety margin (rounded up).
	# 6) Return the final integer.
	n = len(consumption_data) 
	x = []
	for i in range(1, n+1):
		consumption_data[i-1] -= (10 * math.sin(2 *PI * i/ 10))
		x.append(i)
	alpha = np.sum((x - np.mean(x)) * (consumption_data - np.mean(consumption_data))) / np.sum((x - np.mean(x)) ** 2)
	beta = np.mean(consumption_data) - alpha * np.mean(x)
	result = alpha * 15 + beta
	result = result * 1.05
	return math.ceil(result)