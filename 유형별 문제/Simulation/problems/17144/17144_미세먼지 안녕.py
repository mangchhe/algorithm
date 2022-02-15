import copy

input = __import__("sys").stdin.readline


def spread(sX, sY):
    share = room[sX][sY] // 5
    cnt = 0
    for i in range(4):
        x = sX + dx[i]
        y = sY + dy[i]
        if -1 < x < R and -1 < y < C and room[x][y] != -1:
            tmp[x][y] += share
            cnt += 1
    tmp[sX][sY] += room[sX][sY] - share * cnt


def clean(x, y):
    for i in range(x - 1, 0, -1):
        tmp[i][y] = tmp[i - 1][y]
    for i in range(0, C - 1):
        tmp[0][i] = tmp[0][i + 1]
    for i in range(0, x):
        tmp[i][C - 1] = tmp[i + 1][C - 1]
    for i in range(C - 1, y + 1, -1):
        tmp[x][i] = tmp[x][i - 1]
    tmp[x][y + 1] = 0

    x += 1

    for i in range(x + 1, R - 1):
        tmp[i][y] = tmp[i + 1][y]
    for i in range(y, C - 1):
        tmp[R - 1][i] = tmp[R - 1][i + 1]
    for i in range(R - 1, x - 1, -1):
        tmp[i][C - 1] = tmp[i - 1][C - 1]
    for i in range(C - 1, y + 1, -1):
        tmp[x][i] = tmp[x][i - 1]
    tmp[x][y + 1] = 0


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
aircleaner = []
ans = 0

for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            aircleaner.append((i, j))

for _ in range(T):
    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1:
                tmp[i][j] = -1
            elif room[i][j] != 0:
                spread(i, j)

    clean(aircleaner[0][0], aircleaner[0][1])

    room = copy.deepcopy(tmp)

for i in room:
    ans += sum(i)

print(ans + 2)
