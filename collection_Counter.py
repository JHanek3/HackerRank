# Task
# Raghu is a shoe shop owner, his shop has X number of shoes
# He has a list containing the size of each shoe he has in his shop
# There are N number of Customers who are willing to pay x amount of money only if they get the shoe of their desired size
# You task is to compute how much money Raghu has made

# Input Format
# First line contains X number of shoes
# Second line contains the space separated list of all the shoe sizes in the shop
# Third line contains N, number of customers
# The next N lines contain the sepace separated values of the shoe size desired by the customer and x, the price of shoe

#Output Format
# Print the amount of money earned by Raghu

from collections import Counter

def raghu():
  # number of shoes, might not be neccessary
  x = int(input())

  shoe_list = map(int, input().split())
  # shoe_list = [2, 3, 4, 5, 6, 7, 6, 5, 18]

  shoe_inventory = Counter(shoe_list)
  # print(shoe_inventory)
  
  # number of customers
  N = int(input())

  #money earned
  total = 0

  for _ in range(1, N + 1):
    cust = input().split(" ")
    if int(cust[0]) in shoe_inventory:
      if shoe_inventory[int(cust[0])] > 0:
        total += int(cust[1])
        shoe_inventory[int(cust[0])] -= 1
      # print(shoe_inventory)
  print(total)

raghu()