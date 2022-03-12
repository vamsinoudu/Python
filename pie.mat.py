import matplotlib
from matplotlib import pyplot as plot
import numpy as np

# With Pyplot, you can use the pie() function to draw pie charts:
y = np.array([2, 3, 4, 5])
my_labels = ["Books", "Pen", "Notepad", "Pencil"]
plot.pie(y, labels=my_labels)
plot.legend(title="stationary")   # list of items will show and add title to list
plot.show()
