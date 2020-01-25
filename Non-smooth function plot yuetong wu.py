import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, .1)
y = np.absolute(x)
x0 = 0
r = 0.01

fig, axes = plt.subplots(1, 3, figsize=(10,4))
ax1 = axes[0]
ax1.scatter(x0, np.absolute(x0), marker='x')
ax1.plot(x, y)

ax2 = axes[1]
ax2.set_xlim(x0-r, x0+r)
ax2.plot(x, y)

ax3 = axes[2]
ax3.set_xlim(x0-r, x0+r)
ax3.set_ylim(x0, np.absolute(x0+r))
ax3.plot(x, y)
plt.subplots_adjust(wspace=0.4)
plt.show()
