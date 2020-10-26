"""
    작성일 : 20/10/26
"""

import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def solve(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

solve(start)

for i in range(1, n + 1):
    print(distance[i])