# 等差數列與等比數列

import numpy as np
a = np.linspace(10,20,5, endpoint=False)
print(a)

# [10. 12. 14. 16. 18.]

b = np.linspace(0,2,9).reshape(3,3)
print(b)

# [[0.   0.25 0.5 ]
#  [0.75 1.   1.25]
#  [1.5  1.75 2.  ]]

c = np.logspace(0,9,10, base=2, dtype='i4').reshape(2,5)
print(c)

# [[  1   2   4   8  16]
#  [ 32  64 128 256 512]]