# -*- coding: utf-8 -*
import numpy as np

a = np.array([2, 0, 1 ,5])
print(a)
print(a[:3])
print(a.min())
#  由小到大排序
a.sort()
print(a)

#   二维矩阵
b = np.array([[1,2,3], [4,5,6]])
print(b*b)
