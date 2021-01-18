#Task
#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, 
#Otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. 
#It is only necessary to complete the is_leap function.

#Input Format
#Read year, the year to test

#Output Format
#The function returns a Boolena value(True/False)

def is_leap(year):
  leap = False
  if (year % 4 == 0):
    if(year % 100 == 0):
      if (year % 400 == 0):
        leap = True
    else:
      leap = True
  return leap
