# Task
# Given n words, some words may repeat for each word output its number of occurenes
# The output should correspond with the input order of appearance of the word

# Input Format
# The first line contains the integer, n
# The next n lines contain a word

# Output Format
# First line is the number of distinct words from the input
# Second line output the number of occurances for each distinct word

# THIS SOLUTION TIMED OUT, MEANING TOO MANY FOR LOOPS
# from collections import Counter 

# input_words = []
# input_integer = int(input())
# for _ in range(input_integer):
#   x = input()
#   input_words.append(x)

# # outputs number of distinct words
# input_set = set(input_words)
# print(len(input_set))

# # cant use set because you need the order
# final_list = []
# # keeps track of the counts of each word
# final_count = []
# d = Counter(input_words)

# for x in input_words:
#   if x not in final_list:
#     final_list.append(x)
# for x in final_list:
#   final_count.append(str(d[x]))

# print(' '.join(final_count))

from collections import Counter

n = int(input())
# made the input of the words a bit faster? it got condensed to one line
words = [input().strip() for _ in range(n)]

# this doesn't change
count = Counter(words)
# because counter is a dictionary we can count the number of keys
print(len(count))
# prints the key values on one line
print(*count.values())