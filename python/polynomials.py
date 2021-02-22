# Task
# You are given the coefficients of a polynomial P
# Your task is to find the vallue of P at point X

import numpy as np
coef = np.array(list(map(float, input().split())))
x = int(input())
print (np.polyval(coef, x))