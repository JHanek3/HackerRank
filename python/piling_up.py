# Task
# There is a horizontal row of n cubes, the length of each cube is given
# You need to create a new vertical pile of cubes
# If cubei is ontop of cubej then sideLengthj >= sideLengthi
# When stacking the cubes you can only pick up either the leftmost or the rightmost cube each time
# Print yes if is possible ot stack the cubes otherwise print no

# Input Format
# First line contains a single integer T, the number of test cases
# For each test case there are 2 lines
# The first line of each test case contains n, the number of cubes
# The second line contains n space separated integers, denoting the sideLengths of each cube in that order

from collections import deque
# Number of Test Cases
T = int(input())
for _ in range(T):
  n = int(input())
  start_stack = list(map(int, input().split(" ")))


# start_stack = [4, 3, 2, 1, 3, 4]
# start_stack = [1, 3, 2]

  stack_d = deque(start_stack)

  key_stack = sorted(start_stack, reverse=True)
  stack = []

  for x in start_stack:
    if stack_d[0] < stack_d[-1]:
      stack.append(stack_d.pop())
    elif stack_d[0] > stack_d[-1]:
      stack.append(stack_d.popleft())
    elif stack_d[0] == stack_d[-1]:
      stack.append(stack_d.popleft())
    else:
      continue

  if key_stack == stack:
    print("Yes")
  else:
    print("No")

