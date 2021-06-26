import heapq

N = int(input())

def dijkstra(s, graph, distance):
    q = []
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    return distance

for _ in range(N):
    n, m, s = map(int, input().split())
    distance = [float('INF')] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))

    tmp = list(filter(lambda x : x != float('INF'), dijkstra(s, graph, distance)[1:n + 1]))

    print(len(tmp), max(tmp))