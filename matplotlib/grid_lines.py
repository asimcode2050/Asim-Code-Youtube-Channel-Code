import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y)
plt.grid(True)
plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
plt.show()
