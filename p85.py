#指定陣列的資料型態

import numpy as np
a =np.array([1,2,3,4])
print(a)
print(a.dtype)

# [1 2 3 4]
# int32


a =np.array([1,2,3,4],np.int64)
print(a)
print(a.dtype)

# [1 2 3 4]
# int64

a =np.array([1,2,3,4],dtype=float)
print(a)
print(a.dtype)

# [1. 2. 3. 4.]
# float64

a =np.array([1,2,3,4],dtype=complex)
print(a)
print(a.dtype)

# [1.+0.j 2.+0.j 3.+0.j 4.+0.j]
# complex128


b= np.array(a,dtype=float,copy=True)
print(b)
print(b.dtype)

# [1. 2. 3. 4.]
# float64