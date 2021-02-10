# Task
# Given an integer, n, print the following values for each integer i from 1 to n
# Decimal, Octal, Hexadecimal(capitalized), Binary

# Input Format
# A single integer denoting n

# Output Format
# Print n lines where each line i contains the respective decimal, octal, capitalized hexadecimal, and binary values of i
# Each printed value must be formatted to the width of the binary value of n

def print_formatted(n):
  max_width = len(bin(n)[2:])
  for number in range(1, n + 1):
    # Need to remove the o, b, x
    x = oct(number)
    y = x.find('o')
    octal = x[y + 1:]
    
    a = hex(number)
    b = a.find('x')
    hexa = a[b + 1:].upper()


    c = bin(number)
    d = c.find('b')
    binary = c[d + 1:]
    
    print('{:{width}} {:>{width}} {:>{width}} {:>{width}}'.format(number, octal, hexa, binary, width=max_width))
# if __name__ == 'main':
n = int(input())
print_formatted(n)