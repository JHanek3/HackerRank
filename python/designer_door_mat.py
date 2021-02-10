# Task
# Mat size must be N * M (N is an odd natural number and M is 3 times N)
# Design should have welcome written in the center
# The design pattern should only use |,. and - characters
import math

def design_doormat(n, m):
  n = int(n)
  m = int(m)
  max_width = m
  starting_design = ['.', '|', '.']
  row_string = ''.join(starting_design)
  print(row_string.center(max_width, "-"))
  
  row_design = starting_design[:]
  # middle_row or middle_number this value determines when to place the welcome and when to start descending down the list
  middle_row = math.ceil(n / 2)
  
  # 2 is used because the first row is already printed above
  # n + 1 happens because we print the string before we edit the list, kinda seems counter-intuitive
  for number in range(2, n + 1):
    if number < middle_row:
      row_design.extend(starting_design)
      row_design.extend(starting_design)
      row_string = ''.join(row_design)
      print(row_string.center(max_width, "-"))

    elif number == middle_row:
      print("WELCOME".center(max_width, "-"))
    
    else:
      print(row_string.center(max_width, "-"))
      del row_design[0:3]
      del row_design[-3:]
      row_string = ''.join(row_design)

# design_doormat(7, 21)
# design_doormat(11, 33)
# design_doormat(9, 27)

(n,m) = input().split()
design_doormat(n, m)
