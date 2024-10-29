import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, num=500)
y1 = np.sin(5 * x)
y2 = np.cos(5 * x)
y3 = np.cos(5 * x)
y4 = np.cos(5 * x)

fig,axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

axs[0,0].plot(x, y1, color='blue')
axs[0,0].set_title('Axis [0,0]')
axs[0,0].set_xlim(0, 2 * np.pi)

axs[0,1].plot(x, y2, color='orange')
axs[0,1].set_title('Axis [0,1]')
axs[0,1].set_xlim(0, 2 * np.pi)

axs[1,0].plot(x, y1, color='green')
axs[1,0].set_title('Axis [1,0]')
axs[1,0].set_xlim(0, 2 * np.pi)

axs[1,1].plot(x, y2, color='red')
axs[1,1].set_title('Axis [1,1]')
axs[1,1].set_xlim(0, 2 * np.pi)

plt.subplots_adjust(wspace=0.5, hspace=0.5)

# Show the plot
plt.show()
