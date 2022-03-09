import numpy as np

# structured array:
a = np.array([('Bob marley', 2, 21.1), ('Jack', 10, 24)],
             dtype=[('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float64)])
b = np.sort(a, order='name')
print('sorting according to name ', b)
b = np.sort(a, order='age')
print('\nsorting according to the age ', b)
