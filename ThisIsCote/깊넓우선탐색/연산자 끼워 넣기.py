"""
    작성자 : 20/11/12 - PyP3 완료, Python 시간초과
"""

from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
giho = list(map(int, input().split()))
operation = []
o = ['+', '-', '*', '/']
result = []

for idx, i in enumerate(giho):
    for j in range(i):
        operation.append(o[idx])

for i in permutations(operation):

    tmp = data[0]

    for num, op in zip(range(1, n), i):

        if op == '+':
            tmp += data[num]
        elif op == '-':
            tmp -= data[num]
        elif op == '*':
            tmp *= data[num]
        else:
            tmp = int(tmp / data[num])

    result.append(tmp)

print(max(result))
print(min(result))