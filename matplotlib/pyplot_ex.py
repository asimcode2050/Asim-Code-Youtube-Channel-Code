import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, color='blue', marker='o', linestyle='-', label="y = x^2")
plt.title("Simple Plot of y = x^2")
plt.xlabel("X Values")
plt.ylabel("Y Values (x^2)")
plt.grid(True)
plt.legend()
plt.show()
