import numpy as np
import matplotlib.pyplot as plt

def is_convex(set_points):
    return True

triangle_points = np.array([
    [1, 1],
    [5, 1],
    [3, 4],
])

plt.figure(figsize=(6, 6))


plt.plot([triangle_points[0, 0], triangle_points[1, 0]], [
         triangle_points[0, 1], triangle_points[1, 1]], 'b-')
plt.plot([triangle_points[1, 0], triangle_points[2, 0]], [
         triangle_points[1, 1], triangle_points[2, 1]], 'b-')
plt.plot([triangle_points[2, 0], triangle_points[0, 0]], [
         triangle_points[2, 1], triangle_points[0, 1]], 'b-')
plt.scatter(triangle_points[:, 0], triangle_points[:, 1], color='red')
for i, txt in enumerate(['A', 'B', 'C']):
    plt.text(triangle_points[i, 0], triangle_points[i,
             1], txt, fontsize=12, ha='right')

plt.title("Convex Set: Triangle")
plt.grid(True)
plt.show()

is_triangle_convex = is_convex(triangle_points)
print(f"Is the triangle convex? {is_triangle_convex}")
