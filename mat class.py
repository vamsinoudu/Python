import matplotlib

""" 
Matplotlib is one of the most popular Python packages used for data visualization.
Cross-platform library for making 2D plots from data in arrays.

"""
from matplotlib import pyplot as plt

# x axis :
'''
# Line plots:
x = [1,2,9,4,7]
y = [10,5,8,4,2]
plt.plot(x,y)
plt.show()


# Bar plots:
x = [1, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
plt.bar(x, y)
plt.show()

# Histogram plots:       # The graph will show number of elements repeating frequency:
y = [10, 5, 8, 4, 2,10]
plt.hist(y)
plt.show()
'''
# scatter plots:
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
plt.scatter(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Scatter plot")
plt.show()
