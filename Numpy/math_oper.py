import numpy as np
arr = np.array([10,20,30,40,50])
print("Original Array:\n", arr)

# No need of loops for element-wise operations

print(arr + 5)        # Adding scalar to each element
print(arr - 5)        # Subtracting scalar from each element
print(arr * 2)        # Multiplying each element by scalar
print(arr / 2)        # Dividing each element by scalar
print(arr ** 2)       # Squaring each element
print(arr % 3)        # Modulus of each element with scalar
print(np.sqrt(arr))   # Square root of each element

# Aggregation functions
print("Sum:", np.sum(arr))               # Sum of all elements
print("Mean:", np.mean(arr))             # Mean of elements
print("Standard Deviation:", np.std(arr)) # Standard deviation of elements
print("Maximum:", np.max(arr))           # Maximum element
print("Minimum:", np.min(arr))           # Minimum element
print("Median:", np.median(arr))         # Median of elements
print("Cumulative Sum:", np.cumsum(arr)) # Cumulative sum of elements
print("Variance:", np.var(arr))           # Variance of elements
