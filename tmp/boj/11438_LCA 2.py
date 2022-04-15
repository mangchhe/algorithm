import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(now, depth):
    d[now] = depth
    visited[now] = 1
    for i in graph[now]:
        if visited[i]:
            continue
        parent[i][0] = now
        dfs(i, depth + 1)
        
def setParent():
    for i in range(1, H):
        for j in range(1, N + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):
    if d[a] > d[b]:
        a, b = b, a

    for i in range(H, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(H - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

N = int(input())
graph = [[] for _ in range(N + 1)]
d = [0] * (N + 1)
visited = [0] * (N + 1)
H = 18
parent = [[0] * H for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
setParent()

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))
