# inseting ele in arr
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# Inserting elements at specific positions
# insert(value, index, element, axis=None)
# in 2d array to insert data rowise then axis =0 else columnwise axis=1
arr_with_insert = np.insert(arr, 2, 25)  # Insert 25 at index 2
print("Array after insertion:", arr_with_insert)

# appending ele in arr at the end
arr_with_append = np.append(arr, [60, 70])  # Append 60 and 70 at the end
print("Array after appending:", arr_with_append)

# deleting ele in arr
# in 2d array if we want to delete row then axis=0 else column axis=1
arr_with_delete = np.delete(arr, 1)  # Delete element at index 1
print("Array after deletion:", arr_with_delete)

# concatenating two arrays
arr2 = np.array([60, 70, 80])   
concatenated_arr = np.concatenate((arr, arr2))  # Concatenate arr and arr2
print("Concatenated Array:", concatenated_arr)

# stacking arrays vertically and horizontally
arr3 = np.array([90, 100, 110])
vertical_stack = np.vstack((arr, arr2, arr3))  # Vertical stacking
print("Vertically Stacked Array:\n", vertical_stack)
horizontal_stack = np.hstack((arr, arr2, arr3))  # Horizontal stacking
print("Horizontally Stacked Array:", horizontal_stack)

# splitting an array into multiple sub-arrays
split_arr = np.array([10, 20, 30, 40, 50, 60])
sub_arrays = np.array_split(split_arr, 3)  # Split into 3 sub-arrays
print("Sub-arrays after splitting:", sub_arrays)