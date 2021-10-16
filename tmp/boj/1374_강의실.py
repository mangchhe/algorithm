# https://www.acmicpc.net/problem/1374

import heapq

input = __import__('sys').stdin.readline

N = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[2]))
h = [(lectures[0][2], lectures[0][1])]
ans = 1

for i in range(1, len(lectures)):
    n, s, e = lectures[i]
    heapq.heappush(h, (e, s))
    if s >= h[0][0]:
        heapq.heappop(h)
    ans = len(h)

print(ans)
