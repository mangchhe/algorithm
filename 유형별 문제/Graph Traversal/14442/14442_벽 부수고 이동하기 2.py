from collections import deque

input = __import__("sys").stdin.readline

N, M, K = map(int, input().split())
visited = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
arr = [list(input().rstrip()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    visited[x][y][0] = 1
    q = deque([(x, y, 0, 1)])

    while q:
        x, y, v, c = q.popleft()
        if x == N - 1 and y == M - 1:
            return c
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if -1 < tx < N and -1 < ty < M and not visited[tx][ty][v]:
                visited[tx][ty][v] = 1
                if arr[tx][ty] == "1" and v < K:
                    q.append((tx, ty, v + 1, c + 1))
                elif arr[tx][ty] == "0":
                    q.append((tx, ty, v, c + 1))


res = bfs(0, 0)

if res:
    print(res)
else:
    print(-1)
