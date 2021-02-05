# Task
# You are ggiven a date, your task is to find what the day is on that date

# Input Format
# A single line of input containing the space separated month, day, and year respectively in MM DD YYYY Format

# Output Format
# Output the corect day in capital letters

import calendar

def is_day(inpu):
  weekday_list = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
  inpu_list = inpu.split(" ")
  weekday = calendar.weekday(int(inpu_list[2]), int(inpu_list[0]), int(inpu_list[1]))
  print(weekday_list[weekday])

x = input()
is_day(x)