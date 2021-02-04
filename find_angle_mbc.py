# Task
# Angle ABC = 90
# Point M is the midpoint of hypotenuse AC
# You are given lengths AB and BC
# Your task is to find the angle MBC

# Input Format
# The first line contains the length of side AB
# The second line contains the length of side BC

# Output Format
# Output Angle MBC in degrees

import math

x = int(input())
y = int(input())

def find_angle(ab , bc):
  hypotenuse = math.hypot(ab, bc)
  mc = hypotenuse / 2
  degree = round(math.degrees(math.acos(bc / hypotenuse)))
  degree_sign = chr(176)
  print("{}{}".format(degree, degree_sign))

find_angle(x,y)