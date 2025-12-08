# numpy arr with default values
import numpy as np
# with zeros
zeroes_array = np.zeros((2, 2))
print("Array of zeros:", zeroes_array)

# with ones
ones_array = np.ones((3, 3))
print("Array of ones:", ones_array)

# with specific values with full function
full_array = np.full((2, 3), 7)
print("Array filled with 7s:", full_array)

# with arange {start, stop, step} can be given in code.
arange_array = np.arange(1,10,2)    
print("Array with arange:", arange_array)