input = __import__("sys").stdin.readline

N, M = map(int, input().split())

img = [[0] * M for _ in range(N)]
res = 0
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y, t):

    global visited

    q = [(x, y)]
    visited[x][y] = 1
    while q:
        x, y = q.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < N and -1 < ty < M and not visited[tx][ty]:
                if img[tx][ty] >= t:
                    visited[tx][ty] = 1
                    q.append((tx, ty))


for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp) // 3):
        img[i][j] = sum(tmp[0 + (j * 3) : 3 + (j * 3)]) // 3

T = int(input())

for i in range(N):
    for j in range(M):
        if not visited[i][j] and img[i][j] >= T:
            bfs(i, j, T)
            res += 1

print(res)
