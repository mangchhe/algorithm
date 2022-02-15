import heapq

input = __import__("sys").stdin.readline

N = int(input())

work = [tuple(map(int, input().split())) for _ in range(N)]
work.sort()
ans = 0

h = []

for s, e in work:
    if not h or h[0] > s:
        ans += 1
        heapq.heappush(h, e)
    else:
        heapq.heappop(h)
        heapq.heappush(h, e)

print(ans)
