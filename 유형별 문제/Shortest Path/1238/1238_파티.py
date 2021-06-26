import heapq
from sys import stdin

input = stdin.readline

INF = float('INF')
n, m, s = map(int ,input().split())
# res = [0] * (n + 1)
res = 0

graph = [[] for _ in range(n + 1)]
reverseGraph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    reverseGraph[b].append((a, c))


# def dijkstra(start):
#     q = []
#     distance = [INF] * (n + 1)
#     distance[start] = 0
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)
        
#         if dist > distance[now]:
#             continue
#         else:
#             for i in graph[now]:
#                 cost = dist + i[1]
#                 if cost < distance[i[0]]:
#                     distance[i[0]] = cost
#                     heapq.heappush(q, (cost, i[0]))

#     if start == s:
#         for i, val in enumerate(distance):
#             res[i] += val
#     else:
#         res[start] += distance[s]

# for i in range(1, n + 1):
#     dijkstra(i)

# print(max(res[1:]))

def dijkstra(start, graph):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        
        if dist > distance[now]:
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    return distance

forwardDis = dijkstra(s, graph)
reverseDis = dijkstra(s, reverseGraph)

for i in range(1, n + 1):
    res = max(res, forwardDis[i] + reverseDis[i])

print(res)