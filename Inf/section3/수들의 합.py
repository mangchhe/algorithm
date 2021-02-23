import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

data = list(map(int, input().split()))

cnt = 0

val = data[0]
lt, rt = 0, 1

while True:
    if val < m:
        if rt < n:
            val += data[rt]
            rt += 1
        else:
            break
    elif val == m:
        cnt += 1
        if lt < n:
            val -= data[lt]
            lt += 1
        else:
            break
    else:
        if lt < n:
            val -= data[lt]
            lt += 1
        else:
            break

print(cnt)