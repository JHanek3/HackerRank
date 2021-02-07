# Task
# Find the total number of students who have subscribed to at least one newspaper

# Input Format
# integer, the number of students who subscribed to newspaper 1
# contains n, space separated roll numbers of those students
# contains b, the number of students who have subscribed to the french newspaper
# contains b space separated roll numbers of those students

# Output Format
# Total number of students with one subscription

# irrelevant
a = int(input())
x = set(map(int, input().split()))
# irrelevant
b = int(input())
y = set(map(int, input().split()))
z = x.union(y)

print(len(z))