from collections import deque

input = __import__("sys").stdin.readline

N, M = map(int, input().split())
zido = [list(input().rstrip()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs(x, y):
    q = deque([(x, y, 0, 1)])
    visited[x][y][0] = 1
    while q:
        nx, ny, nv, nCnt = q.popleft()
        if nx == N - 1 and ny == M - 1:
            return nCnt
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and not visited[tx][ty][nv]:
                visited[tx][ty][nv] = 1
                if zido[tx][ty] == "0":
                    q.append((tx, ty, nv, nCnt + 1))
                elif nv == 0:
                    q.append((tx, ty, 1, nCnt + 1))


res = bfs(0, 0)

print(res if res != None else -1)
