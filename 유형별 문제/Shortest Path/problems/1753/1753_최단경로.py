import heapq

input = __import__("sys").stdin.readline


def solve():

    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

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


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
distance = [float("INF")] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

solve()

for i in range(1, V + 1):
    if distance[i] != float("INF"):
        print(distance[i])
    else:
        print("INF")
