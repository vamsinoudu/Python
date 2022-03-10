import numpy as np
'''
# 1 D array:
arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x)

# 2 D array:
arr_1 = np.array([[1, 2, 3, 7], [4, 5, 6, 8]])
for x in arr_1:
    print(x)
# spliting into array:
arr_2 = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr_2,3)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])

#spliting 2-D array:
arr_3 =np.array([[1,2],[3,4],[5,6]])
new_arr = np.array_split(arr_3,3)
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])
'''
# 3D array:
a_3d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a_3d_array)


