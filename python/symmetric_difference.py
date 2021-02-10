# Task
# Use symmetric difference on two sets. That are in the set iterable but not both

# irrelevant
a = int(input())
x = set(map(int, input().split()))
# irrelevant
b = int(input())
y = set(map(int, input().split()))
z = x.symmetric_difference(y)

print(len(z))