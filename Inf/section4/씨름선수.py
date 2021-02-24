import sys

#sys.stdin = open('input.txt', 'rt')

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x : -x[0])

wei = data[0][1]
cnt = 0

for d in data:

    if wei > d[1]:
        cnt += 1
    else:
        wei = d[1]

print(n - cnt)