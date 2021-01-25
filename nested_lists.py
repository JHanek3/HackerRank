# Task
# Given the names and grades for each student in a class of N students, store them in a nested list 
# and print the names of any students having the second lowest grade

# Input Format
# The first line contains an integer, N, the number of students
# The 2N subsequent lines describe each student over 2 lines
# The first line contains the student's name
# The second line contains their grade

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade

# Output Format
# Print the name(s) of any students having the second lowest grade. If there are multiple students, order their
# names alphabetically and print each one on a new line

def nested_list():
  records = []
  for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
  # print(records)
  # records = [["beta", 50.0], ["alpha", 50.0], ["chi", 20.0], ["delta", 60.0]]
  
  # Sort the records based on test scores
  sorted_records = sorted(records, key = lambda x: x[1])
  # print(sorted_records)

  output_list = []
  lowest_val = sorted_records[0][1]
  # print(lowest_val)
  
  for x,y in sorted_records:
    if y == lowest_val:
      continue
    if y > lowest_val:
      second_lowest_val = y
      break
  # print(x, y)
  
  #Found the second lowest grade, now search the list for it
  for x,y in sorted_records:
    if y == second_lowest_val:
      output_list.append(x)
  # print(second_lowest_val)

  # Output of printing multiple students on a new line and sorted alphabetically
  output_list.sort()
  for x in output_list:
    print(x)
    

nested_list()