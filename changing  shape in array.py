import numpy as np
# number of element in arr.we need to reshape.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(3,4)
print(new_arr)

# float and Negative
arr = np.array([1, 2.2, 3.5, 4.6, 5, 6, 7, 8, 9, -10, -11, -12])
new_arr = arr.reshape(3,4)
print(new_arr)

# string:
arr = np.array(['krishna', 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(3,4)
print(new_arr)
