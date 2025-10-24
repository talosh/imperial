# 2D vector operations and visualisation

import matplotlib.pyplot as plt
import numpy as np

# Define 2D vectors
v1 = np.array([3, 4])
v2 = np.array([2, 1])

# Vector operations
v_add = v1 + v2
v_sub = v1 - v2
dot_product = np.dot(v1, v2)

# Set up 2D plot
plt.figure(figsize=(8, 8))

# Plot original vectors
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'v1 = {v1}')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label=f'v2 = {v2}')

# Plot vector addition and subtraction
plt.quiver(0, 0, v_add[0], v_add[1], angles='xy', scale_units='xy', scale=1, color='g', alpha=0.6, label='v1 + v2')
plt.quiver(0, 0, v_sub[0], v_sub[1], angles='xy', scale_units='xy', scale=1, color='m', alpha=0.6, label='v1 - v2')

# Axes and plot settings
plt.xlim(-2, 8)
plt.ylim(-2, 8)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("2D Vector Operations")

# Show plot
plt.show()
