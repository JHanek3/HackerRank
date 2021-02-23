# Task
# You are given a a Square matrix A with dimensions N*N
# Find the determinant and round to 2 decimal places

import numpy as np
N = int(input())
A = np.array([input().split() for _ in range(N)], float)
# A = np.array([[1.1, 1.1],
#             [1.1, 1.1]
# ])
print(round(np.linalg.det(A),2))