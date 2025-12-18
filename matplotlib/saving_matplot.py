# with savefig() function we can save current fig in our machine/system 
# in Any format, with filename, shairng also possible.

# savefig('filename.extension', dpi = value, bbox_inches = 'tight')
# dpi -> control image resolution

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,18]

plt.plot(x, y, color = 'blue', marker = 'o')
plt.title("Simple line plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.savefig(r'C:\Users\HP\OneDrive\Pictures\Screenshots\Line_Plot.png', dpi=300, bbox_inches='tight')
plt.show()