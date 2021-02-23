import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

# for i in range(n // 2):
#     for j in range(1 + (i * 2)):
#         result += data[i][n // 2 - i + j]
#         result += data[n - i - 1][n // 2 - i + j]

# for i in range(n):
#     result += data[n // 2][i]

# print(result)

res = 0
s = e = n // 2

for i in range(n):
    for j in range(s, e + 1):
        res += data[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)