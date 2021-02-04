# Task
# You are given a complex z. Your task is to convert it to polar coordinates

# Input Format
# A single line containing the comple number z.
# Note: complex() function can be used in python to convert the input as a complex number

# Output Format
# The first line should contain the value of r
# The second lline should contain the value of phase angle

import cmath
def polar_coordinates(inp):
  print(abs(complex(inp)))
  print(cmath.phase(complex(inp)))
  

x = input()

polar_coordinates(x)


