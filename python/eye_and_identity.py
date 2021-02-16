# The identity tool returns an identity array, an identity array is a square matrix with all the main diagonal elements as 1 and the rest as 0
# The default type of the element is a float

# The eye tool returns a 2-D array with 1's as the diagnol and 0's elsewhere
# The diagnoal can be main, upper or lower depending on the optional parameter k
# A positive k is for the upper diagonal and a negative k is for the lower, and a 0 K is for the main diagonal

# Task
# Your task is to print an array of size N*M with its main diagonal elements as 1's and and 0's everywhere else

import numpy

(n, m)= map(int,input().split())

print(numpy.eye(n,m, k = 0))