import matplotlib.pyplot as plt

product = ['A','B','C','D','E']
sales = [1000, 1500, 2000, 800, 888]

plt.bar(product, sales, color = 'orange', label = "Sales 2025")
# if we want horizontal then we can used 'barh'
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.legend()

plt.show()

