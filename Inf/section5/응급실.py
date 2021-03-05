import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

data = deque(list(map(int, input().split())))

cnt = 0

target = m

while True:

    cur = data.popleft()

    for i in range(n - 1):
        if cur < data[i]:
            data.append(cur)
            if target == 0:
                target = n - 1
            else:
                target -= 1
            break
    else:
        cnt += 1
        if target == 0:
            print(cnt)
            break
        else:
            n -= 1
            target -= 1