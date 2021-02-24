# Task
# You are given string s
# Your task is to find all the substrings of S that contains 2 or more vowels
# Substrings must lie in between 2 consonants and should contain vowels only

import re
# S = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
S = input()
# S = "abaabaabaabaae"
# ?= is a look ahead only matches if followed exactly
reg = re.findall(r"(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU])", S)
if reg:
  for x in reg:
    print(x)
else:
  print(-1)