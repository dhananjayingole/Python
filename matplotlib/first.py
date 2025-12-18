import matplotlib.pyplot as plt

x = ['Mon','Tue','Wed','Thur','Fri']
y = [10,15,7,20,12]

# plt.plot(x, y, color='color name', linestyle = 'line_style',linewidth = value, marker=marker symbol, label='label name')

plt.plot(x,y, color = 'green',linestyle = '--',linewidth = 2, marker = 0, label='2025 sales data')
plt.title('Bakery Sales this Week!') # to set the title or headline of the Graph.
plt.legend(loc='upper left')
plt.xlabel('Day of the week')
plt.ylabel('Sales per Day')

plt.grid(color='gray',linestyle=':', linewidth= 2)
plt.ylim(0, 25)

plt.xticks(['Mon','Tue','Wed','Thur','Fri'] , ['day1','day2','day3','day4','day5'])
plt.show()