# handling of Missing or error values in numpy arrays
import numpy as np
# Creating an array with some missing values (NaN)
arr = np.array([1, 2, np.nan, 4, 5, np.nan, 7])
print("Original array with NaN values:", arr)
# Identifying NaN values
nan_mask = np.isnan(arr) # it detects the nan values in arr
print("NaN mask:", nan_mask)
# Handling NaN values by replacing them with the mean of the non-NaN elements
mean_value = np.nanmean(arr) # calculates mean ignoring nan values
print("Mean value (ignoring NaN):", mean_value)
arr_filled = np.where(nan_mask, mean_value, arr) # replace nan with mean value
print("Array after replacing NaN with mean value:", arr_filled)

