input = __import__("sys").stdin.readline
R, C = map(int, input().split())
lake = [list(input().rstrip()) for _ in range(R)]
bVisited = [[0] * C for _ in range(R)]
waterB = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0
flag = True

for i in range(R):
    for j in range(C):
        if lake[i][j] == "L":
            birdB = [(i, j)]
            waterB.append((i, j))
        elif lake[i][j] == ".":
            waterB.append((i, j))

bVisited[birdB[0][0]][birdB[0][1]] = 1

while flag:

    birdN = []
    waterN = []

    while birdB:
        x, y = birdB.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < R and -1 < ty < C:
                if not bVisited[tx][ty]:
                    bVisited[tx][ty] = 1
                    if lake[tx][ty] == ".":
                        birdB.append((tx, ty))
                    elif lake[tx][ty] == "X":
                        birdN.append((tx, ty))
                    elif lake[tx][ty] == "L":
                        flag = False
                        break
        if not flag:
            break

    if not flag:
        break

    birdB = birdN

    while waterB:
        x, y = waterB.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < R and -1 < ty < C:
                if lake[tx][ty] == "X":
                    lake[tx][ty] = "."
                    waterN.append((tx, ty))

    waterB = waterN
    ans += 1

print(ans)
