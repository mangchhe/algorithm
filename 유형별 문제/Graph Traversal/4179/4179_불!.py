input = __import__("sys").stdin.readline


def next_fire():
    global fire
    tmp = []
    while fire:
        nx, ny = fire.pop()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and not fireVisited[tx][ty]:
                fireVisited[tx][ty] = 1
                if maze[tx][ty] not in ["#", "F"]:
                    maze[tx][ty] = "F"
                    tmp.append((tx, ty))

    fire = tmp


def next_human():
    global human
    tmp = []
    while human:
        nx, ny = human.pop()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if -1 < tx < N and -1 < ty < M and not humanVisited[tx][ty]:
                humanVisited[tx][ty] = 1
                if maze[tx][ty] == ".":
                    maze[tx][ty] = "J"
                    tmp.append((tx, ty))

    human = tmp


def findEdge():
    for i in range(N):
        if maze[i][0] == "J" or maze[i][M - 1] == "J":
            return True
    for i in range(M):
        if maze[0][i] == "J" or maze[N - 1][i] == "J":
            return True
    return False


N, M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
fire = []
human = []
fireVisited = [[0] * M for _ in range(N)]
humanVisited = [[0] * M for _ in range(N)]
minute = 0

for i in range(N):
    for j in range(M):
        if maze[i][j] == "F":
            fire.append((i, j))
        elif maze[i][j] == "J":
            human.append((i, j))

while True:
    if findEdge():
        print(minute + 1)
        break
    else:
        minute += 1
    if next_human():
        break
    if not human:
        print("IMPOSSIBLE")
        break
    next_fire()
