# Task
# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. 
# Your initial happiness is 0. For each i integer in the array, if i == A, you add 1 to your happiness. If i == B , you add -1 to your happiness. 
# Otherwise, your happiness does not change. Output your final happiness at the end.

# Input Format
# The first line contains integers n and m separeted by a space
# The second line contains n integers, the elements of the array
# The third line and fourth line contain m integers, A and B respectively

# Output Format
# Output a single integer, your total happiness

def my_happiness(x,y,z,a):
  total_happiness = 0
  useless = x

  master_list = y.split(" ")
  
  A = set(z.split(" "))
  B = set(a.split(" "))
  
  print(sum((i in A) - (i in B) for i in master_list))

x = input()
y = input()
z = input()
a = input()
my_happiness(x,y,z,a)