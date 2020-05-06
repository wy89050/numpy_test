#自訂結構型態

import numpy as np
# int8, int16, int32, int64 可用 'i1', 'i2','i4','i8'代替
# float16, float32, float64 可用 'f1', 'f2','f4' 代替

dt = np.dtype('f2')
print(dt)

people = np.dtype([('name','S20'), ('height', 'i4'), ('weight', 'f2')])

a = np.array([('amy', 156, 50),('bob', 175, 72)], dtype = people )
print(a)
print(a['name'])
print(a['weight'])
print(len(a['name']))
print(type(a['name'][0]))
print(type(a['height'][0]))