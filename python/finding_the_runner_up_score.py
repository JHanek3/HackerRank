#Task
#Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.

#Input Format
#The first line contains n. The second line contains an array A[]
#of n integers each seperated by a space

#Output Format
#Print the runner-up score

A = list(arr)
vMax = max(A)
A.sort(reverse=True)
for x in A:
  if x == vMax:
    continue
  else:
    print(x)
    break