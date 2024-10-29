import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, num=500)
y1 = np.sin(5 * x)
y2 = np.cos(5 * x)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

ax1.plot(x, y1, color='blue')
ax1.set_title('Axis [0]')
ax1.set_xlim(0, 2 * np.pi)

ax2.plot(x, y2, color='green')
ax2.set_title('Axis [1]')
ax2.set_xlim(0, 2 * np.pi)

plt.subplots_adjust(wspace=0.5)

# Show the plot
plt.show()
