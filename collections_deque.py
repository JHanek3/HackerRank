# A deque is a double-ended queue, it can be used to add or remove elements from both ends
# Deques support thread safe, memory efficeint appends and pops from either side of the deque with aproximately the same 
# performance in either direction

# Task
# Perform append, pop, popleft and appendleft methods on an empty deque d

# Input Format
# The first line contains an integer N, the number of operations
# The next N lines contains the space separated names of methods and their values

# Output Format
# Print the space separated elements of deque d

from collections import deque
d = deque()

n = int(input())

for _ in range(n):
  action = input()
  action_string = action.split(" ")
  if action_string[0] == "append":
    d.append(int(action_string[1]))
  elif action_string[0] == "appendleft":
    d.appendleft(int(action_string[1]))
  elif action_string[0] == "pop":
    d.pop()
  elif action_string[0] == "popleft":
    d.popleft()
  else:
    continue

print(*d)
