#建立陣列

import numpy as np

a = np.array([1,2,3])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# [1 2 3]
# 1
# (3,)
# 3
# int32

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)

# [[1 2 3]
#  [4 5 6]]
# 2
# (2, 3)
# 6
# int32


c =np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype)

# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
# 3
# (2, 2, 2)
# 8
# int32


