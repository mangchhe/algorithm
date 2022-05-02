import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    h = [(0, start)]
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            totalDis = dist + i[1]
            if distance[i[0]] > totalDis:
                distance[i[0]] = totalDis
                heapq.heappush(h, (totalDis, i[0]))
                route[i[0]] = now

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [float('INF')] * (N + 1)
route = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())

dijkstra(s)

ans = []
idx = e
while idx != s:
    ans.append(idx)
    idx = route[idx]

ans.append(s)

print(distance[e])
print(len(ans))
print(*ans[::-1])
