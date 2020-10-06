"""
    작성일 : 20/10/06
"""

n = int(input())

data = []

for i in range(n):
    input_data = input().split()
    data.append((input_data[0], int(input_data[1])))

""" 
? lambda student: student[1] : 두번째 원소 기준으로 정렬
+ key = lambda student: (student[0], -student[1])
첫번째 요소를 오름차순으로 정렬 후 두번째 요소를 내림차순으로 정렬
"""
data = sorted(data, key=lambda student: student[1])

for student in data:
    print(student)
