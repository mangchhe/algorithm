def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def melt(x, y):
    cnt = 0
    for cx, cy in move(x, y):
        if cx < 0 or cx >= R or cy < 0 or cy >= C:
            cnt += 1
        elif arr[cx][cy] == '.':
            cnt += 1

    return True if cnt >= 3 else False

def getXY():
    sx, sy = R, C
    ex, ey = 0, 0

    for i in range(R):
        for j in range(C):
            if tmp[i][j] == 'X':
                sx, sy = min(sx, i), min(sy, j)
                ex, ey = max(ex, i), max(ey, j)

    return sx, sy, ex, ey

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
tmp = [['.'] * C for _ in range(R)]
ans = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == '.':
            continue
        tmp[i][j] = '.' if melt(i, j) else 'X'
            
sx, sy, ex, ey = getXY()

for i in range(sx, ex + 1):
    ans.append(tmp[i][sy : ey + 1])

for i in ans:
    print(''.join(i))
