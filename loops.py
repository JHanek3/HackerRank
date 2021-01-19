#Task
#The provided code stub reads an integer,n, from STDIN. For all non-negative integers i < n, print .
#print i^2

#Input Format
#The first and only line contains the integer n.

#Output Format
#Print n lines, one corresponding to each i,

def square():
    n = int(input())
    for i in range(n):
        if i >= 0:
            print(i**2)

square()
