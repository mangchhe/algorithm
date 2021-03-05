import sys
from collections import deque

# sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())

data = deque([i for i in range(1, n + 1)])

res = 0
cnt = 0

while data:
    cnt += 1
    if cnt != k:
        data.append(data.popleft())
    else:
        res = data.popleft()
        cnt = 0

print(res)