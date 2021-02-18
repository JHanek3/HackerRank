# Task
# Given a 2-D array with dimensions NxM
# Your task is to perform the sum tool over xios 0 and then find the product of that result

import numpy as np

(N,M) = map(int,input().split())
# print(N, M)
my_array = np.array([input().split() for _ in range(N)], int)

# print(my_array)
x = np.sum(my_array, axis=0)
y = np.prod(x, axis=None)
# print(x)
print(y)