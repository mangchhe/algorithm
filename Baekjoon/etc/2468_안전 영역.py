from functools import reduce

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
maxVal = max(reduce(lambda x, y: x + y, map))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
res = 0


def bfs(x, y, visited):
    visited[x][y] = 1
    q = [(x, y)]
    while q:
        x, y = q.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < n and -1 < ty < n and visited[tx][ty] == 0:
                visited[tx][ty] = 1
                q.append((tx, ty))


for k in range(0, maxVal):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if map[i][j] <= k:
                visited[i][j] = 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j, visited)
                cnt += 1

    res = max(res, cnt)

print(res)
