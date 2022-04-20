import heapq
input = __import__('sys').stdin.readline

def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, (start, 0))

    while h:
        now, dist = heapq.heappop(h)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            c = dist + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(h, (i[0], c))

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [float('INF')] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dijkstra(1)

print(distance[N])
