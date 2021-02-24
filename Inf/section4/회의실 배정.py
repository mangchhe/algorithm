import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x: (x[1], x[0]))

bef = 0
res = 0

for d in data:
    if bef <= d[0]:
        bef = d[1]
        res += 1

print(res)