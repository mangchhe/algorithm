from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

input = __import__('sys').stdin.readline

def findPillar(root):
    cost = 0
    node = root
    visited[node] = 1

    while graph[node]:
        if len(graph[node]) > 2 or (len(graph[node]) == 1 and node != root) or (len(graph[node]) == 2 and node == root):
            return (node, cost)
        else:
            for i in graph[node]:
                if not visited[i[0]]:
                    visited[i[0]] = 1
                    cost += i[1]
                    node = i[0]

    return (node, cost)

def dfs(node, cost):

    global branch

    if len(graph[node]) == 1:
        branch = max(branch, cost)
    else:
        for i in graph[node]:
            if not visited[i[0]]:
                visited[i[0]] = 1
                dfs(i[0], cost + i[1])


N, R = map(int, input().split())
graph = defaultdict(list)
branch = 0
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

node, pillar = findPillar(R)

dfs(node, 0)

print(pillar, branch)
