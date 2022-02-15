from collections import deque

input = __import__("sys").stdin.readline


def bfs(node):
    visited = [0] * (N + 1)
    q = deque([(node, 0)])
    visited[node] = 1
    ret = (0, 0)
    while q:
        now = q.popleft()
        if len(graph[now[0]]) == 1:
            if ret[1] < now[1]:
                ret = (now[0], now[1])
        for i in graph[now[0]]:
            if not visited[i[0]]:
                q.append((i[0], i[1] + now[1]))
                visited[i[0]] = 1

    return ret


N = int(input())
ans = 0
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

print(bfs(bfs(1)[0])[1])
