"""
    작성일 : 20/10/24
"""

import sys

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())

visited = []
distance = []
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

x, k = map(int, input().split())

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def solve(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

result = 0

for i, j in [[1, k], [k, x]]:
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)
    solve(i)
    if distance[j] == INF:
        print(-1)
        break
    else:
        result += distance[j]
        if j == x:
            print(result)