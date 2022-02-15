input = __import__("sys").stdin.readline


def bfs(sx, sy):

    party = [(sx, sy)]
    q = [(sx, sy)]
    visited[sx][sy] = 1

    while q:
        nowX, nowY = q.pop()
        for i in range(4):
            x = nowX - dx[i]
            y = nowY - dy[i]
            if -1 < x < N and -1 < y < N and not visited[x][y]:
                if L <= abs(land[x][y] - land[nowX][nowY]) <= R:
                    visited[x][y] = 1
                    q.append((x, y))
                    party.append((x, y))

    if len(party) == 1:
        return 0
    else:
        tmp = sum(map(lambda e: land[e[0]][e[1]], party)) // len(party)
        for i in party:
            land[i[0]][i[1]] = tmp

        return 1


N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1
ans = 0

while True:

    cnt = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += bfs(i, j)

    if not cnt:
        break

    ans += 1

print(ans)
