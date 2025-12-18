import matplotlib.pyplot as plt

# plt.hist(data, bins = number_of_bins, color='colorname', edgecolor='black')

scores = [48,95,65,75,99,88,73,76,81,90,44,28,33,58,52,68,63,83,77]
plt.hist(scores, bins=5, color='green', edgecolor= 'orange')
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.title("Score Distribution of Students")
plt.show()