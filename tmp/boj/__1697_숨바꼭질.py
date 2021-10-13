# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs(start, cost):
    q = deque([(start, cost)])
    visited[start] = 1
    while q:
        now = q.popleft()
        if now[0] == M:
            print(now[1])
            break
        if now[0] - 1 > -1 and not visited[now[0] - 1]:
            visited[now[0] - 1] = 1
            q.append((now[0] - 1, now[1] + 1))
        if now[0] + 1 < 100001 and not visited[now[0] + 1]:
            visited[now[0] + 1] = 1
            q.append((now[0] + 1, now[1] + 1))
        if now[0] * 2 < 100001 and not visited[now[0] * 2]:
            visited[now[0] * 2] = 1
            q.append((now[0] * 2, now[1] + 1))

N, M = map(int, input().split())
visited = [0] * 100001

bfs(N, 0)
