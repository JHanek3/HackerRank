# Task
# You are given a 2-D array with dimensions NxM
# Your task is to perform the min function over axis 1 and then find the max of that

import numpy as np

(N,M) = map(int,input().split())
# # print(N, M)
my_array = np.array([input().split() for _ in range(N)], int)
# my_array = np.array([
#   [2 ,5],
#   [3, 7],
#   [1, 3],
#   [4, 0]
# ])
# print(my_array)
print(np.max(np.min(my_array, axis=1)))