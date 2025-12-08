import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d.shape) # Output: (2, 3) -> which shows 2 rows and 3 columns    
print(arr_2d.size)  # Output: 6 -> total number of elements in the array
print(arr_2d.ndim)  # Output: 2 -> number of dimensions
print(arr_2d.dtype) # Output: int32 (or int64 depending on the system) -> data type of the elements
          
# changine data type using astype() 
arr_float = arr_2d.astype(np.float64)
print(arr_float)
print(arr_float.dtype) # Output: float64 -> data type after conversion 

# reshaping array using reshape()
reshaped_arr = arr_2d.reshape(3, 2)
print(reshaped_arr)