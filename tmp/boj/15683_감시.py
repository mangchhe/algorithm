# https://www.acmicpc.net/problem/15683

input = __import__('sys').stdin.readline

def move(x, y, direction):
    ret = []
    for d in direction:
        if d == 'l':
            for i in range(y, -1, -1):
                if room[x][i] == 6:
                    break
                elif room[x][i] == 0:
                    room[x][i] = '#'
                    ret.append((x, i))
        elif d == 'r':
            for i in range(y, M):
                if room[x][i] == 6:
                    break
                elif room[x][i] == 0:
                    room[x][i] = '#'
                    ret.append((x, i))
        elif d == 'u':
            for i in range(x, -1, -1):
                if room[i][y] == 6:
                    break
                elif room[i][y] == 0:
                    room[i][y] = '#'
                    ret.append((i, y))
        elif d == 'd':
            for i in range(x, N):
                if room[i][y] == 6:
                    break
                elif room[i][y] == 0:
                    room[i][y] = '#'
                    ret.append((i, y))
    return ret

def traverse(n):
    global ans
    if n >= len(cctvs):
        total = 0
        for i in range(N):
            for j in range(M):
                if room[i][j] == 0:
                    total += 1
        ans = min(ans, total)
    else:
        for d in directions[cctvs[n][0]]:
            ret = move(cctvs[n][1], cctvs[n][2], d)
            traverse(n + 1)
            for r in ret:
                room[r[0]][r[1]] = 0

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
directions = {
    1 : [['l'], ['r'], ['u'], ['d']],
    2 : [['l', 'r'], ['u', 'd']],
    3 : [['u', 'r'], ['r', 'd'], ['d', 'l'], ['l', 'u']],
    4 : [['l', 'u', 'r'], ['u', 'r', 'd'], ['r', 'd', 'l'], ['d', 'l', 'u']],
    5 : [['l', 'u', 'r', 'd']]
}

cctvs = []
ans = float('INF')

for i in range(N):
    for j in range(M):
        if 0 < room[i][j] < 6:
            cctvs.append((room[i][j], i, j))

traverse(0)

print(ans)
