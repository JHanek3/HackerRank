# Task
# Given a 1-D array, A. Task is to print the floor, ceil and rint of all elements of A

import numpy as np

A = list(map(float,input().split()))
A = np.array(A)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))