# Task
# Apply your knowledge of the .add() operation to help your friend Rupal
# Rupal has a huge collection of country stamps, she decided to count the total number of distinct country stamps in her collection
# She asked for your help, find the total number of distinct country stamps

# Input Format
# The first line contains an integer N, the total number of Country Stamps
# The next N lines contains the name of the country from where the stamp is from

# Output Format
# Output the total number of distinct country stamps on a single line

distinct_countries = set()
n = int(input())
for _ in range(n):
  country = input()
  distinct_countries.add(country)
print(len(distinct_countries))
