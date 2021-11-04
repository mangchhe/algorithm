from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
ans = -1

def bfs(x, y):
    global ans
    q = deque([(x, y, 0)])

    while q:
        nx, ny, nc = q.popleft()
        
        if nx == r2 and ny == c2:
            ans = nc
            break

        for i in range(6):
            cx = nx + dx[i]
            cy = ny + dy[i]
            if cx < 0 or cx > N - 1 or cy < 0 or cy > N - 1 or board[cx][cy]:
                continue

            board[cx][cy] = 1
            q.append((cx, cy, nc + 1))

N = int(input())
board = [[0] * N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())

bfs(r1, c1)

print(ans)
