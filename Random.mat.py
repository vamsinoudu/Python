import matplotlib
from matplotlib import pyplot as plot
import numpy as np

# create random arrays with 100 values for x-points, y-points, colors and sizes:

x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 5 * np.random.randint(100, size=100)

plot.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plot.colorbar()
plot.show()
