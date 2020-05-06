# 矩陣計算

import numpy as np
a = np.arange(6).reshape(3,2)
print(a)
print('')

b = np.arange(6).reshape(2,3)
print(b)
print('')

c = np.dot(a,b)
#矩陣內積
print(c)
print('')

print(c.T)
#矩陣轉置