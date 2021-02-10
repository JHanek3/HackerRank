#Task
#The provided code stub will read in a dictionary ocntaining key/value pairs of name: [marks] for a list of students.
#Print the average of the marks array for the student name provided, showing 2 places after the decimal

#Input Format
#First line contains the integer n, number of student records
#Second line contain the names and the marks obtained by a student each value separated by a space
#Third line contains query_name

#Output Format
#Print one line: The average of the marks obtained by the particular student correct to 2 decimal places

import statistics
def finding_percent():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    pretty = statistics.mean(student_marks[query_name])
    print('{:.2f}'.format(pretty))

finding_percent()