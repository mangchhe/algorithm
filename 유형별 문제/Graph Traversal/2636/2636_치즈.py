input = __import__("sys").stdin.readline


def bfs():
    global hour, q, cheeseCnt
    tmp = []
    while q:
        nx, ny = q.pop()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and not visited[tx][ty]:
                visited[tx][ty] = 1
                if cheese[tx][ty] == 0:
                    q.append((tx, ty))
                else:
                    tmp.append((tx, ty))
        if not q:
            if tmp:
                cheeseCnt = len(tmp)
                hour += 1
            q = tmp
            tmp = []


N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cheese = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = []
hour = 0
cheeseCnt = 0

for i in range(M):
    if cheese[0][i] == 0:
        q.append((0, i))
        visited[0][i] = 1
    if cheese[N - 1][i] == 0:
        q.append((N - 1, i))
        visited[N - 1][i] = 1

for i in range(1, N - 1):
    if cheese[i][0] == 0:
        q.append((i, 0))
        visited[i][0] = 0
    if cheese[i][M - 1] == 0:
        q.append((i, M - 1))
        visited[i][M - 1] = 1

bfs()

print(hour)
print(cheeseCnt)
