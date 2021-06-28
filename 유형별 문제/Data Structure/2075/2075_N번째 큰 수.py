import heapq

input = __import__("sys").stdin.readline

N = int(input())
h = []

for i in range(N):
    for j in map(int, input().split()):
        heapq.heappush(h, j)
    if i > 0:
        for _ in range(N):
            heapq.heappop(h)

print(h[0])
