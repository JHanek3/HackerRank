# Task
# You are given two integer arrays, A and B of dimensions NxM
# Add A + B
# Subtract A - B
# Multiply A * B
# Integer Division A / B
# Mod A % B
# Power A ** B

import numpy

(N, M) = map(int,input().split())
A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

# For some reason the output needs to look like
# [[6 8 10 12]]
print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(numpy.floor(numpy.divide(A, B)).astype(int))
print(numpy.mod(A, B))
print(numpy.power(A, B))

