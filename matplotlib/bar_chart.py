import matplotlib.pyplot as plt
import numpy as np
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
bar_width = 0.35
index = np.arange(len(categories))
values1 = [3, 7, 2, 5]
values2 = [4, 6, 3, 8]
plt.bar(index, values1, bar_width, label='Group 1', color='blue')
plt.bar(index + bar_width, values2, bar_width, label='Group 2', color='orange')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Grouped Bar Chart')
plt.xticks(index + bar_width / 2, categories)
plt.legend()
plt.show()
