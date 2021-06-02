from sys import stdin
import heapq

input = stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra(n, graph):

    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))
    distance = [[float('INF')] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        else:
            for i in range(4):
                x, y = now[0] + dx[i], now[1] + dy[i]
                if -1 < x < n and -1 < y < n:
                    cost = dist + graph[x][y]
                    if cost < distance[x][y]:
                        distance[x][y] = cost
                        heapq.heappush(q, (cost, (x, y)))

    return distance[n - 1][n - 1]

cnt = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    print('Problem {}: {}'.format(cnt, dijkstra(n, graph)))

    cnt += 1