import heapq

input = __import__("sys").stdin.readline

cnt = 0
ans = 0
h = []

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[0], x[1]))

for s, t in arr:
    if not h:
        heapq.heappush(h, t)
        cnt += 1
    else:
        if h and h[0] <= s:
            heapq.heappop(h)
            cnt -= 1

        heapq.heappush(h, t)
        cnt += 1

    ans = max(ans, cnt)

print(ans)
