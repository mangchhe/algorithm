import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

data = list(map(int, input().split()))

res = [n + 1 for i in range(n)]

for i, d in enumerate(data):

    cnt = d

    for j in range(n):

        if cnt == 0 and res[j] == n + 1:
            res[j] = i + 1
            break

        if res[j] > i + 1:
            cnt -= 1

for i in res:
    print(i, end=' ')