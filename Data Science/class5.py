import numpy as np

arr1 = np.array([[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1,]] dtype='i32')

print(arr1)


import numpy as np

arr1 = np.array([[3, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1,]])

print(arr1)

print(arr1.ndim)
print(arr1.size)
print(arr1.shape)
print(arr1.dtype)


import numpy as np

arr1 = np.array([[3.1, 3, 3, 3], [2, 2, 2, 2], [1, 1, 1, 1,]])

print(arr1)


arr2 = arr1.astype(np.float32)

print(arr2.dtype)

arr1 = np.array([[2.,2.],[4.,5.]])

print(1/arr1)


arr1 = np.array([[2.,2.],[4.,5.]])

print(arr1 ** 2)


arr1 = np.array([[2.,2.],[4.,5.]])

print(arr1 > arr1)


arr1 = np.array([[2.,2.],[4.,5.]])

print(arr1 * 3)


arr1 = np.array([[2.,2.],[4.,5.]])

print(arr1 - 2)


