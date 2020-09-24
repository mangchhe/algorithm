""" 
    작성일 : 20/09/23
"""

from sys import stdin

n, m , k = map(int, stdin.readline().split())

data = list(map(int, stdin.readline().split()))

data.sort()

result = 0

for i in range(1, m + 1):

    if i % k != 0:

        result += data[-1]

    else:

        result += data[-2]

print(result)