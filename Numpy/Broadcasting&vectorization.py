# Applying a fixed discount to a list of prices using broadcasting
# without using explicit loops.
# lets try first with loops
prices = [100, 200, 300, 400, 500]
discount = 10

final_prices = []

for price in prices:
    final_price = price - (price * discount / 100)
    final_prices.append(final_price)

print("Final prices after discount:", final_prices)

# Now using numpy and broadcasting
import numpy as np
prices = np.array([100, 200, 300, 400, 500])
# Discount percentage
discount = 10  # 10 percent discount
final_prices = prices - (prices * discount / 100)
print("Final prices after discount using broadcasting:", final_prices)
# mutliplication examples
result = prices * 2
print("Prices multiplied by 2:", result)

#  1d to 2d broadcasting
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
vector = np.array([10, 20, 30])
result = matrix + vector
print("Matrix after adding vector using broadcasting:\n", result)

# vectorization example
def compute_square(arr):
    return arr ** 2 
arr = np.array([1, 2, 3, 4, 5])
squared_arr = compute_square(arr)   
print("Squared array using vectorization:", squared_arr)

