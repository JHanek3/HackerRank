# Task
# You are given a string, split the string on a " " space delimeter and join using a - hyphen

# Input Format
# The first line contains a string consisting of space separated words

# Output Format
# Print the formatted strings as explained above.

def split_and_join(line):
  split = line.split(' ')
  join = "-".join(split)
  print(join)

split_and_join("this is a string")

