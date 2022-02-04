import heapq

input = __import__('sys').stdin.readline

N = int(input())
mettings = [tuple(map(int, input().split())) for _ in range(N)]
h = []
ans = 0

mettings.sort()

for i in range(N):
    s, e = mettings[i]

    while h and h[0] <= s:
        heapq.heappop(h)

    heapq.heappush(h, e)
    ans = max(ans, len(h))

print(ans)
