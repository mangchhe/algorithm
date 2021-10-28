# https://www.acmicpc.net/problem/16928

from collections import deque

def bfs(x):
    q = deque([x])
    visited[x] = 0

    while q:
        now = q.pop()
        if zump.get(now):
            if visited[zump[now]] > visited[now]:
                visited[zump[now]] = visited[now]
                q.append(zump[now])
        else:
            for i in range(1, 7):
                if now + i < 101 and visited[now + i] > visited[now] + 1:
                    visited[now + i] = visited[now] + 1
                    q.append(now + i)

N, M = map(int, input().split())
visited = [float('INF')] * 101
zump = {}

for _ in range(N + M):
    s, e = map(int, input().split())
    zump[s] = e

bfs(1)

print(visited[100])
