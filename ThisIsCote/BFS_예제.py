"""
    작성일 : 20/09/25
"""

from collections import deque

def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visitedNode.append(i)
                queue.append(i)
                visited[i] = True
        
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

bfs(graph, 1, visited)

print(visitedNode)