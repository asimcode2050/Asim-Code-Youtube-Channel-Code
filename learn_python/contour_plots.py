import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-0.1 * (X**2 + Y**2))
plt.figure(figsize=(8, 6))
contour = plt.contour(X, Y, Z, levels=10, cmap='viridis')
plt.clabel(contour, inline=True, fontsize=8)
plt.title("Contour Plot of 2D Gaussian")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.colorbar(contour)
plt.show()
