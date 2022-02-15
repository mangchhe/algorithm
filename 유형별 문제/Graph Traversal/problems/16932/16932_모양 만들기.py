input = __import__("sys").stdin.readline


def bfs(x, y, c):
    visited[x][y] = 1
    arr[x][y] = c
    cnt = 1
    q = [(x, y)]
    while q:
        nx, ny = q.pop()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and not visited[tx][ty]:
                visited[tx][ty] = 1
                if arr[tx][ty] == 1:
                    q.append((tx, ty))
                    arr[tx][ty] = c
                    cnt += 1
    return cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

c = 1
cList = {0: 0}
res = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1:
            cList[c] = bfs(i, j, c)
            c += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            tmp = 0
            tmpSet = set()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if -1 < x < N and -1 < y < M:
                    tmpSet.add(arr[x][y])
            for k in tmpSet:
                tmp += cList[k]

            res = max(res, tmp)

print(res + 1)
