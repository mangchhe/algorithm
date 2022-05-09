import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    q = deque([(x, y)])
    dis = 0

    while q:
        x, y = q.popleft()

        for cx, cy in move(x, y):
            if cx < 0 or cx > N - 1 or cy < 0 or cy > M - 1 or visited[cx][cy] or treasure[cx][cy] == 'W':
                continue
            visited[cx][cy] = visited[x][y] + 1
            dis = max(dis, visited[cx][cy])
            q.append((cx, cy))

    return dis - 1

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

N, M = map(int, input().split())
treasure = [list(input()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        if treasure[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)
