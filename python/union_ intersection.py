# Task find who have subscribed to both newspapers
# Input Format same as previous
# Output Format
# Number of both subscriptions

# irrelevant
a = int(input())
x = set(map(int, input().split()))
# irrelevant
b = int(input())
y = set(map(int, input().split()))
z = x.intersection(y)

print(len(z))