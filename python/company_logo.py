# Task
# Newly opened company wants to base their logo on the three most common characters in the company name
# Given a string s, find the top three most common characters in the string
# Print the three most common characters along with their occurences count
# sort in descending order of occurence count
# if occurence count the same sort in alphabetical order

from collections import Counter

inp = input()
# inp = "qwertyuiopasdfghjklzxcvbnm"
# inp = "aabbbccde"

sorted_string = ''.join(sorted(inp))
iterator = 0
for value, count in Counter(sorted_string).most_common():
  print(value, count)
  iterator += 1
  if iterator == 3:
    break;