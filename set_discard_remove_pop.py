 # .remove(x)
 # Removes element x from the set, if x DNE it raises a key error, returns None

 # .discard(x)
 # Also removes element x from the set but does not reaise a key error, returns None

 #.pop()
 # This operation removes and return an arbitrary element from the set
 # No elements to remove, it raises a KeyError

 # Task
 # You have a non-empty s and you have to execute N commands given in N lines
 # The commands will be pop, remove and discard

 # Input Format
 # The first line contains integer m the number of elements in the set s
 # The second line contains n space separated elements of set s.
 # The third line contains integer N, the number of commands
 # The next N lines contains either pop, remove, and or discard commands

 # Output Format
 # Print the sum of the leements of set s on a single line

# the number of elements in set S
n = int(input())

# n space separated elements of set S
s = set(map(int, input().split()))

# number of commands
z = int(input())

# The commands
for _ in range(z):
  command = input()
  if command[0] == "d":
    s.discard(int(command[-1]))
  elif command[0] == "r":
    try:
      s.remove(int(command[-1]))
    except:
      continue
  else:
    s.pop()
print(sum(s))