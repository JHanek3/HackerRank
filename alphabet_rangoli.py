# Task
# You are given an integer N. Your task is to print an alphabet rangoli of size N
# The center of the rangoli has the first alphabet letter a, and the boundry has the Nth alphabet letter

# Input Format
# Only one line of input containing N, the size of the rangoli

# Output Format
# Print the alphabet rangoli in the format explain above

def print_rangoli(size):
  max_width = size * 4 - 3
  # print(max_width)
  row_list = []
  for letter in range(96 + size, 96, -1):
    if row_list == []:
      row_list.append(chr(letter))
      row_string = '-'.join(row_list)
      print(row_string.center(max_width, "-"))
    else:
      row_list.append(chr(letter))
      other_half_of_list = row_list[:len(row_list) - 1]
      other_half_of_list.reverse()
      row_final = row_list + other_half_of_list
      row_string = '-'.join(row_final)
      print(row_string.center(max_width, "-"))

  # Above code prints the first 60% of the rangoli, now we need to print the other
  remaining_lines = size - 1
  for x in range(remaining_lines):
    row_list.pop()
    other_half_of_list = row_list[:len(row_list) -1]
    other_half_of_list.reverse()
    row_final = row_list + other_half_of_list
    row_string = '-'.join(row_final)
    print(row_string.center(max_width, "-"))

# print_rangoli(3)
print_rangoli(26)