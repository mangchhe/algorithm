import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(now, depth):
    d[now] = depth
    visited[now] = 1

    for i in graph[now]:
        if visited[i]:
            continue
        parent[i] = now
        dfs(i, depth + 1)

def lca(a, b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
        
    return a

N = int(input())
d = [0] * (N + 1)
parent = [0] * (N + 1)
graph = {i : [] for i in range(1, N + 1)}
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))
