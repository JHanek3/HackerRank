#Task
#Read a given string, change the character at a given index and then print the modified string.

#Input Format
#The first line constains a string, S
#The next line contains an integer , denoting the index location and a character  separated by a space.

#Output Format
#USing any of the methods explained above, reaplce the character at index i with character c.

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]