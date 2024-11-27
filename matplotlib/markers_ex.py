import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
plt.plot(x, y, marker='o', markersize=8,
         color='blue', linestyle='-', linewidth=2)
plt.plot(x, y, marker='s', markerfacecolor='red', markeredgewidth=2,
         markersize=10, color='green', linestyle='-')
plt.xlabel('X-Axis')  # Labels the x-axis as 'X-Axis'
plt.ylabel('Y-Axis')  # Labels the y-axis as 'Y-Axis'
plt.title('Scatter Plot with Custom Markers')  # Gives the plot a title
plt.show()
