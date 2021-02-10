#Task
#You are asked to ensure that the first and last names of people begin 
# with a capital letter in their passports.

#Input Format
#A single line of input containing the full name S

#Output Format
#Print the capitalized string, S

def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s