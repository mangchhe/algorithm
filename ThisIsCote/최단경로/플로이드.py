"""
    작성일 : 20/10/23
    ! 다익스트라 알고리즘
    ! 하나의 노드에서 다른 노드로 이동할때 의 간선이 두개이상일 경우
    ! distance 초기값을 넣을때 더 낮은 값으로 비교해서 넣어야함
"""

import sys

""" 
    ! 다익스트라 알고리즘 
"""
""" input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
distance = []
visited = []
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def smallest_node_distance():
    min_value = INF
    idx = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            idx = i
    return idx

def solve(start):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        if distance[i[0]] == INF:
            distance[i[0]] = i[1]
        else:
            if distance[i[0]] > i[1]:
                distance[i[0]] = i[1]
    for i in range(n - 1):
        now = smallest_node_distance()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    solve(i)
    del distance[0]
    print(' '.join(map(str, [i if i != INF else 0 for i in distance]))) """

"""
    ! 플로이드 워셜 알고리즘
"""

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')
    print()