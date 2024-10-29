import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.grid(True)

x_min , x_max = -10, 10
y_min , y_max = -10, 10

x_grid_unit, y_grid_unit = 1, 1

x = np.linspace(x_min, x_max, 400)
y = (1/100) * x**3

ax.plot(x, y)

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

ax.set_xticks(np.arange(x_min, x_max + 1, x_grid_unit))
ax.set_yticks(np.arange(y_min, y_max + 1, y_grid_unit))

ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

ax.set_aspect("equal")
plt.title("y = (1/100)x^3")

plt.show()