import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2, 2 * np.pi, 0.1)
print(x)
y = np.sin(x)
plt.plot(x, y)
plt.show()
