"""
    작성일 : 20/10/06
"""

n = int(input())

data = []

for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

""" 
? lambda student: student[1]
"""
data = sorted(data, key=lambda student: student[1])

for student in data:
    print(student)
