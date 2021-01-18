#Task
#The provided code stub reads two integers, a and b, from STDIN.
#Add logic to print two lines. The first line should contain the result of integer a//b division,
#The second line should contain the result of float division,  a/b .
#No rounding or formatting is necessary.

#Input Format
#The First line contains the first integer, a
#The Second line contains the second integer, b

#Output Format
#Print the two lines as described above.

def div():
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

div()