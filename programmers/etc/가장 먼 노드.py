from collections import deque


def bfs(s, nodes, visited, distance):
    cnt = 0

    queue = deque([s])
    visited[s] = 1
    while queue:
        v = queue.popleft()
        for node in nodes[v]:
            if not visited[node]:
                visited[node] = 1
                queue.append(node)
                distance[node] = distance[v] + 1

    return len(list(filter(lambda x: x == max(distance), distance)))


def solution(n, edge):
    answer = 0
    nodes = {}
    visited = [0] * (n + 1)
    distance = [0] * (n + 1)

    for i in edge:
        s, e = i
        if s in nodes:
            nodes[s].append(e)
        else:
            nodes[s] = [e]
        if e in nodes:
            nodes[e].append(s)
        else:
            nodes[e] = [s]

    answer = bfs(1, nodes, visited, distance)

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))