import os
import matplotlib as plt
import numpy as np

x = np.linspace([-1: 1: 1000])
y = np.sin(x)

plt.plot(x, y, '--')
