"""
    작성일 : 20/10/26
"""

"""
    ! 다익스트라 알고리즘
"""

import sys

INF = int(1e9)

input = sys.stdin.readline

n, m, s = map(int, input().split())

visited = [False] * (n + 1)
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def solve(start):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
solve(s)
result = list(filter(lambda x : x != INF, distance))
print(len(result) - 1, max(result))