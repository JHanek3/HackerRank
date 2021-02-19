# Task
# Givena  2-D array of NxM
# Mean along axis 1
# Var along axis 0
# std along axis None

import numpy as np

(N,M) = map(int,input().split())
# print(N, M)
my_array = np.array([input().split() for _ in range(N)], int)
# my_array = np.array([
#   [1 ,2],
#   [3, 4]
# ])
print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print(np.round(np.std(my_array, axis=None), 11))