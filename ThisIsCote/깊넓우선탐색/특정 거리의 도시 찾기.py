"""
    작성일 : 20/10/16
"""

import sys
from collections import deque

input = sys.stdin.readline

INF = 312,345
result = []
n, m, k, x = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs():
    count = 0
    visited[x] = True
    queue = deque(graph[x])

    while True:
        count += 1
        if count > k:
            break
        for i in range(len(queue)):
            current = queue.popleft()
            if not visited[current]:
                if count == k:
                    result.append(current)
                else:
                    queue.extend(graph[current])
    return result

result = bfs()

if result:
    for i in result:
        print(i)
else:
    print(-1)