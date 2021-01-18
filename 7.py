
#Input Format
#The included code stub will read an integer, n, from STDIN
#Without using any string methods, try to print the following
#123...n

#Input Format
#The first line contains an integer n

#Output Format
#Print the list of integers from 1 through n as a string, without spaces

eList = []
for x in range(1, n + 1):
    eList.append(str(x))
print("".join(eList))