#Task
#You are given a string S.
#Your task is to find out if the string S contains: alphanumeric characters, digits, lowercase and
#uppercase characters

#Output Format
#Print True if alphanumeric
#Print True if alphabetical
#Print True if digits
#Print True if lowercase
#Print True if uppercase

def alpha():
    s = input()
    aNumer = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for x in s:
        if x.isalnum():
            aNumer = True
        if x.isalpha():
            alpha = True
        if x.isdigit():
            digit = True
        if x.islower():
            lower = True
        if x.isupper():
            upper = True
    print(aNumer)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)