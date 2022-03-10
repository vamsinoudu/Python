# copy:
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[3] = 42
print(arr)  # copy
print(x)  # orginal

# View:
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[4] = 42
print(arr)  # Both are copied
print(x)

# concatenate:
arr = np.array([1, 2, 3, 4])
new_arr = arr.copy()
arr[2] = 100
y = np.concatenate((arr, new_arr))          #joining
print(arr)
