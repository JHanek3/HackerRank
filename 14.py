#Task given an integer, n, and n space-separated integers as input, create a tupe t of those n integers
#Then compute and print result of hash(t)

#Input Format
#The first line contains an integer, n denoting the number of elements in the tuple
#The second line contains n space-separated integers describing the elements in tuple t

#Output Format
#Print the result of hash(t)

def tup():
  n = int(input())
  integer_list = map(int, input().split())
  tupled = tuple(integer_list)
  print(tupled)
  print(hash(tupled))

tup()