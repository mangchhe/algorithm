"""
    작성일 : 20/09/25
"""

def dfs(graph, v, visited):

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visitedNode.append(i)
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]]

visitedNode = [1,]
visited = [False] * 9

dfs(graph, 1, visited)

print(visitedNode)