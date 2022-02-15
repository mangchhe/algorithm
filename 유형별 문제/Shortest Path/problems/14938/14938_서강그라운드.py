import heapq

input = __import__("sys").stdin.readline

MI = lambda: map(int, input().split())


def solve(start):

    itemCnt = items[start]
    visited = [0] * (N + 1)
    visited[start] = 1
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = i[1] + dist
            if cost <= M:
                if not visited[i[0]]:
                    visited[i[0]] = 1
                    itemCnt += items[i[0]]
                heapq.heappush(q, (cost, i[0]))

    return itemCnt


N, M, R = MI()
items = [0] + list(MI())
graph = [[] for _ in range(N + 1)]
ans = 0
for _ in range(R):
    a, b, c = MI()
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, N + 1):
    ans = max(ans, solve(i))

print(ans)
