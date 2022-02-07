from collections import deque

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    sheep, wolf = 0, 0
    if yard[x][y] == 'v':
        wolf += 1
    elif yard[x][y] == 'o':
        sheep += 1

    while q:
        nx, ny = q.popleft()
        for cx, cy in move(nx, ny):
            if -1 < cx < R and -1 < cy < C and not visited[cx][cy]:
                if yard[cx][cy] == '#':
                    continue
                elif yard[cx][cy] == 'v':
                    wolf += 1
                elif yard[cx][cy] == 'o':
                    sheep += 1
                visited[cx][cy] = 1
                q.append([cx, cy])

    if sheep > wolf:
        ans[0] += sheep
    else:
        ans[1] += wolf

R, C = map(int, input().split())
yard = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
ans = [0, 0]

for i in range(R):
    for j in range(C):
        if not visited[i][j] and yard[i][j] != '#':
            bfs(i, j)

print(*ans)
