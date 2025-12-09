import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Inserting elements at specific positions
arr_with_insert = np.insert(arr, 2, 25)  # Insert 25 at index 2
print("Array after insertion:", arr_with_insert)

# appending ele in arr at the end
arr_with_append = np.append(arr, [60, 70])  # Append 60 and 70 at the end
print("Array after appending:", arr_with_append)

# deleting ele in arr
arr_with_delete = np.delete(arr, 1)  # Delete element at index 1
print("Array after deletion:", arr_with_delete)

# concatenating two arrays
arr2 = np.array([60, 70, 80])   
concatenated_arr = np.concatenate((arr, arr2))  # Concatenate arr and arr2
print("Concatenated Array:", concatenated_arr)

# stacking arrays vertically and horizontally
# FIX: Use arrays with consistent dimensions

# OPTION 1: Reshape to 2D arrays
arr_reshaped = arr.reshape(1, -1)  # Reshape to (1, 5)
arr2_reshaped = arr2.reshape(1, -1)  # Reshape to (1, 3)

print("\n--- OPTION 1: With reshaping ---")
print(f"arr shape after reshape: {arr_reshaped.shape}")
print(f"arr2 shape after reshape: {arr2_reshaped.shape}")

# OPTION 2: Create arrays with same dimensions from the beginning
print("\n--- OPTION 2: Arrays with same dimensions ---")
arr_small = np.array([10, 20, 30])
arr2_small = np.array([60, 70, 80])
arr3_small = np.array([90, 100, 110])

# Now vertical stacking will work (all have 3 elements)
vertical_stack = np.vstack((arr_small, arr2_small, arr3_small))
print("Vertically Stacked Array:\n", vertical_stack)
print(f"Shape of vertical stack: {vertical_stack.shape}")

horizontal_stack = np.hstack((arr_small, arr2_small, arr3_small))
print("Horizontally Stacked Array:", horizontal_stack)
print(f"Shape of horizontal stack: {horizontal_stack.shape}")

# OPTION 3: Column stacking (for 1D arrays)
print("\n--- OPTION 3: Using column_stack for 1D arrays ---")
# Column_stack converts 1D arrays to columns in a 2D array
col_stack = np.column_stack((arr_small, arr2_small, arr3_small))
print("Column Stacked Array:\n", col_stack)
print(f"Shape of column stack: {col_stack.shape}")
