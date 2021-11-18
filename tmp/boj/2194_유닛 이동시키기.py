from collections import deque

input = __import__('sys').stdin.readline

def detect_obstacle(x, y):
    for i in range(x, x + A):
        for j in range(y, y + B):
            if obstacle[i][j] == 1:
                return False
    return True

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def traverse(x, y):
    global ans

    q = deque([(x, y, 0)])
    visited[x][y] = 1

    while q:
        x, y, dist = q.popleft()
        if x == ex and y == ey:
            ans = dist
            break
        for cx, cy in move(x, y):
            if 0 < cx and cx + A - 1 <= N and 0 < cy and cy + B - 1 <= M and detect_obstacle(cx, cy) and not visited[cx][cy]:
                visited[cx][cy] = 1
                q.append((cx, cy, dist + 1))


N, M, A, B, K = map(int, input().split())
obstacle = [[0] * (M + 1) for _ in range(N + 1)]
visited = [[0] * (M + 1) for _ in range(N + 1)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = -1

for _ in range(K):
    x, y = map(int, input().split())
    obstacle[x][y] = 1

sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

traverse(sx, sy)

print(ans)
