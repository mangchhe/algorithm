import heapq
from sys import stdin

input = stdin.readline

maxH = []
minH = []

N = int(input())

for _ in range(N):
    n = int(input())
    if len(maxH) >= len(minH):
        heapq.heappush(minH, -n)
    else:
        heapq.heappush(maxH, n)

    if maxH and minH:
        maxVal = heapq.heappop(maxH)
        minVal = heapq.heappop(minH)
        if maxVal < -minVal:
            minVal, maxVal = -maxVal, -minVal
        heapq.heappush(minH, minVal)
        heapq.heappush(maxH, maxVal)

    tmp = heapq.heappop(minH)
    print(-tmp)
    heapq.heappush(minH, tmp)
