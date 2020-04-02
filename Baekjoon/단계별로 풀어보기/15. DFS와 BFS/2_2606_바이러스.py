from collections import deque

def bfs(graph, start_node):

    visited = []
    queue = deque([start_node])

    while queue:

        current_node = queue.popleft()

        if current_node not in visited:

            visited.append(current_node)
            queue.extend(graph[current_node])

    return visited

graph = {}

input()
for _ in range(int(input())):
    start, end = map(int, input().split())

    if start not in graph:
        graph[start] = [end]
    else:
        graph[start].append(end)

    if end not in graph:
        graph[end] = [start]
    else:
        graph[end].append(start)

print(len(bfs(graph,1)) -1)

