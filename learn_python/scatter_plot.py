import matplotlib.pyplot as plt
# This will help us create the plot
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50) + 0.5 * np.random.randn(50)
print("x values:", x[:5])
print("y values:", y[:5])
plt.scatter(x, y, color='blue', marker='o')
plt.title('Random Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.show()
