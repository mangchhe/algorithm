input = __import__("sys").stdin.readline


def check_earth():
    arr = []
    cnt = 1
    visited = [[0] * M for _ in range(N)]
    for i in q:
        arr.append((i[0], i[1]))
        visited[i[0]][i[1]] = 1
        break
    while arr:
        nx, ny = arr.pop()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and not visited[tx][ty]:
                visited[tx][ty] = 1
                if ice[tx][ty] != 0:
                    arr.append((tx, ty))
                    cnt += 1
    return True if cnt != earthCnt else False


def next_year():
    global earthCnt, ice
    tmp = []
    after_ice = [[0] * M for _ in range(N)]
    result = False
    for nx, ny in q:
        cnt = 0
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and ice[tx][ty] == 0:
                cnt += 1

        after_ice[nx][ny] = max(0, ice[nx][ny] - cnt)
        if after_ice[nx][ny] == 0:
            tmp.append((nx, ny))
            earthCnt -= 1
    for i in tmp:
        result = True
        q.remove(i)
    ice = after_ice
    return result


N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = set()
earthCnt = 0
year = 0

for i in range(N):
    for j in range(M):
        if ice[i][j] != 0:
            q.add((i, j))
            earthCnt += 1

isCheck = True

while True:
    if isCheck:
        if check_earth():
            print(year)
            break
    next_year()
    if not q:
        print(0)
        break
    year += 1
