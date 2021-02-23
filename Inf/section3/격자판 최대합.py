import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

result = 0

for i in range(n):
    tmp = tmp2 = 0
    for j in range(n):
        tmp += data[i][j]
        tmp2 += data[j][i]
    if tmp > result:
        result = tmp
    if tmp2 > result:
        result = tmp2

tmp = tmp2 = 0

for i in range(n):
    tmp += data[i][i]
    tmp2 += data[i][n - i - 1]
else:
    if result < tmp:
        result = tmp
    if result < tmp2:
        result = tmp2

print(result)
    
