#Tasks
#Given 3 integers x,y,z representing the dimensions of a cuboid along with an integer n
#Print a list of possible coordinates given by (i, j, k) on a 3D grib where the sum of i + j +k is not equal to n
#0 <= i <= x; 0 <= j <= y; 0 <= k <= z
#Please use list comprehension

#Input Form 
#four integers, z,y,z, and n

#Constraint
#Print the list in lexicographic increasing order

#Output Form
#Print the list of lists

def list_comprehension():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # x = 1
    # y = 1
    # z = 2
    # n = 3
    final_list = []
    for a in range(x+1):
      for b in range(y + 1):
        for c in range(z + 1):
          final_list.append([a, b, c])
          # print(a, b, c)
    final_list.sort()
    print([ele for ele in final_list if sum(ele) != n])

list_comprehension()