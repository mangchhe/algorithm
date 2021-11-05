from collections import defaultdict
import heapq

input = __import__('sys').stdin.readline

def dijkstra(start, target):
    h = [start]
    dis[start] = 0

    while h:
        now = heapq.heappop(h)

        if dis[now] >= dis[now] + 1:
            continue

        for i in mov[now]:
            if dis[now] + 1 < dis[i]:
                dis[i] = dis[now] + 1
                heapq.heappush(h, i)

A, B = map(int, input().split())
N, M = map(int, input().split())
dis = [float('INF')] * (N + 1)
mov = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    mov[b].append(a)
    mov[a].append(b)

dijkstra(B, A)

print(dis[A] if dis[A] != float('INF') else -1)
