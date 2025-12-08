# indexing in arr
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# Accessing elements using indexing
print("First element:", arr[0])        # First element
print("Last element:", arr[-1])        # Last element
print("Elements from index 1 to 3:", arr[1:4])  # Slicing from index 1 to 3
print("Elements at even indices:", arr[::2])  # Elements at even indices
print("Elements at even indices:", arr[::-1]) # Reversing the array  

# boolean masking -> use conditioning to filter elements without using loops.
print(arr[arr > 25]) # Elements greater than 25
print(arr[(arr % 20) == 0]) # Elements divisible by 20

# reshaping
arr2d = np.array([[1, 2, 3, 4, 5, 6],
                  [7, 8, 9, 10, 11, 12],    
                  [13, 14, 15, 16, 17, 18]])                   
print("Original 2D Array:\n", arr2d)
reshaped_arr = arr2d.reshape(2, 9)  # Reshaping -> (rows, columns)
print("Reshaped Array (2x9):\n", reshaped_arr)