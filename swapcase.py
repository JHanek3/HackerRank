# Task
# You are given a string and your task is to swap cases

# Input Format
# A Single Line Containing a String S

# Output Format
# Print modified string

def swap_case(s):
  swaped_str = ''
  for char in s:
    if ( 90 >= ord(char) >= 65):
      swaped_str += char.lower()
    elif (122 >= ord(char) >= 61):
      swaped_str += char.upper()
    else:
      swaped_str += char
  print(swaped_str)
  # Yo that's lame, you can just use s.swapcase() What's the point of the challenge then?

swap_case("Www.HackerRank.com")
swap_case("HackerRank.com presents \"Pythonist 2\".")