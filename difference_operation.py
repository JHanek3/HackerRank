# Task
# Given two set use difference and print the len of the set

# irrelevant
a = int(input())
x = set(map(int, input().split()))
# irrelevant
b = int(input())
y = set(map(int, input().split()))
z = x.difference(y)

print(len(z))