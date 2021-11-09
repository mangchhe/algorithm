from collections import deque
input = __import__('sys').stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 0

    while q:
        nx, ny = q.popleft()
        for i in range(8):
            cx = nx + dx[i]
            cy = ny + dy[i]
            if 0 < cx < N + 1 and 0 < cy < N + 1 and visited[cx][cy] > visited[nx][ny] + 1:
                visited[cx][cy] = visited[nx][ny] + 1
                q.append((cx, cy))

N, M = map(int, input().split())
nightX, nightY = map(int, input().split())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

visited = [[float('INF')] * (N + 1) for _ in range(N + 1)]

bfs(nightX, nightY)

for _ in range(M):
    x, y = map(int, input().split())
    print(visited[x][y])
