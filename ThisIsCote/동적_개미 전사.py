"""
    작성일 : 20/10/08
"""

n = int(input())

nList = list(map(int, input().split()))

d = [0] * n

d[0] = nList[0]
d[1] = nList[1]

for i in range(2, n):

    d[i] = max(d[i - 1], nList[i] + d[i - 2])

print(d[n - 1])