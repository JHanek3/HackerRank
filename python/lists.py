#Task
#Initialize your list and read in the value of n followed by n lines of commands where each command iwll be of the 7 types listed above.
#Iterate through each command in order and perform the corresponding opertation on your list

#Input Format
#The first line contains an integer, n, denoting the number of commands
#Each line i of the n subsequent lines contains one of the commands described above

#Output Format
#Fir each command of type print, print the list of a new line

import re
def list_commands():
    n = int(input())
    # commands = ["append 1", "append 2", "insert 3 1", "print"]
    # commands = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
    commands = []
    final_list = []
    for _ in range(n):
        command = input()
        commands.append(command)
    
    # print(commands)
    for x in commands:
      # print(x)
      if x == "print":
        print(final_list)
      #a for append
      if x[0] == "a":
        #need to make the single list into a str, then into an integer
        value = int(''.join(re.findall(r'\d+', x)))
        final_list.append(value)
      #needed for remove, and reverse distinguishing
      if x[0:3] == "rem":
        value = int(''.join(re.findall(r'\d+', x)))
        final_list.remove(value)
      if x[0] == "s":
        final_list.sort()
      if x[0:3] == "rev":
        final_list.reverse()
      if x[0:2] == "po":
        final_list.pop()
      if x[0] == "i":
        regex = re.findall(r'\d+', x)
        final_list.insert(int(regex[0]), int(regex[1]))

list_commands()