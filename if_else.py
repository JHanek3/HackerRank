#Task
#If n is odd, print Weird
#If n is even and in the inclusive range of  to , print Not Weird
#If n  is even and in the inclusive range of  to , print Weird
#If n is even and greater than , print Not Weird

#Input Format
#A single line containing a positive integer, n

#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

def weird():
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    else:
        print("Not a valid n")

weird()