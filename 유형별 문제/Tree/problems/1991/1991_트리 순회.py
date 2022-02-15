from collections import defaultdict

input = __import__("sys").stdin.readline

N = int(input())
graph = defaultdict(list)
ans = [[], [], []]

for _ in range(N):
    a, b, c = input().split()
    graph[a].append(b)
    graph[a].append(c)


def dfs(n, graph):
    ans[0].append(n)
    if graph[n][0] != ".":
        dfs(graph[n][0], graph)
    ans[1].append(n)
    if graph[n][1] != ".":
        dfs(graph[n][1], graph)
    ans[2].append(n)


dfs("A", graph)

for i in ans:
    print("".join(i))
