import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

data = []

for i in range(n):
    data.append(int(input()))

data.sort()

s, e = 1, data[-1]
res = 0

def Count(mid):
    tot = 0
    for i in range(n):
        tot += data[i] // mid
    return tot

while s < e:

    mid = (s + e) // 2
    tot = Count(mid)

    if tot < m:
        e = mid - 1
    else:
        res = mid
        s = mid + 1

print(res)