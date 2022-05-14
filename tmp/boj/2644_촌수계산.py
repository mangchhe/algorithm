import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        n = len(q)
        for _ in range(n):
            now = q.popleft()
            if now == end:
                print(visited[now] - 1)
                exit()

            for _next in graph[now]:
                if visited[_next]:
                    continue
                visited[_next] = visited[now] + 1
                q.append(_next)

N = int(input())
start, end = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(start)

print(-1)
