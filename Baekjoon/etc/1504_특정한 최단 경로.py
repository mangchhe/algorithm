import heapq

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]


def dijkstra(s, graph):

    q = []
    distance = [float("INF")] * (n + 1)
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    return distance


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

tmp1 = dijkstra(v1, graph)
tmp2 = dijkstra(v2, graph)

dist1 = tmp1[1] + tmp2[n]
dist2 = tmp1[n] + tmp2[1]
dist3 = tmp1[v2]

if dist1 + dist3 == float("INF") and dist2 + dist3 == float("INF"):
    print(-1)
elif dist1 > dist2:
    print(dist2 + dist3)
else:
    print(dist1 + dist3)
