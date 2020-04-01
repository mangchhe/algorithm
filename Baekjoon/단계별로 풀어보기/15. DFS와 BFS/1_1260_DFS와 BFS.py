from collections import deque
from sys import stdin

def dfs(graph, start_node):

    stack = deque([start_node])
    visited = []

    while stack:
        current_node = stack.popleft()

        if current_node not in visited:
            visited.append(current_node)
            stack.extendleft(graph[current_node][::-1])

    return visited

def bfs(graph, start_node):

    queue = deque([start_node])
    visited = []

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.append(current_node)
            queue.extend(graph[current_node])

    return visited

A, B, start_node = map(int, input().split())

graph = {}

for _ in range(B):
    start, end = map(int,stdin.readline().strip().split())
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]
    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

for i in graph.keys():
    graph[i].sort()

for i in dfs(graph, start_node):
    print(i,end=' ')
print()
for i in bfs(graph, start_node):
    print(i,end=' ')
print()