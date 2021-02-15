# Task
# You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions
# task is to print an array of the given shape and integer type using the tools numpy.zeroes and numpy.ones

import numpy

inp = list(map(int,input().split()))

print(numpy.zeros((inp), dtype = numpy.int))

print(numpy.ones((inp), dtype = numpy.int))