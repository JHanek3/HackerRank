# Task
# Given 2 array A and B, both have dimensions N
# Task is to compute their matrix product

import numpy as np

N = int(input())
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

print(np.matmul(A, B))