input = __import__('sys').stdin.readline

R, C = map(int, input().split())
pasture = [list(input().rstrip()) for _ in range(R)]
sheep = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    for j in range(C):
        if pasture[i][j] == 'W' or pasture[i][j] == '.':
            continue
        sheep.append((i, j))
        for k in range(4):
            cx = i + dx[k]
            cy = j + dy[k]
            if -1 < cx < R and -1 < cy < C:
                if pasture[cx][cy] == 'W':
                    print(0)
                    exit()

for x, y in sheep:
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if -1 < cx < R and -1 < cy < C:
            if pasture[cx][cy] == '.':
                pasture[cx][cy] = 'D'

print(1)
for i in pasture:
    print(''.join(i))
