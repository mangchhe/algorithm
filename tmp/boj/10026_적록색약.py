import copy

def dfs(x, y, color):
    visited[x][y] = 1
    q = [(x, y)]

    while q:
        x, y = q.pop()
        for cx, cy in move(x, y):
            if cx < 0 or cx > N - 1 or cy < 0 or cy > N - 1 or visited[cx][cy]:
                continue
            if picture[cx][cy] in color:
                q.append((cx, cy))
                visited[cx][cy] = 1

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

N = int(input())
picture = [list(input()) for _ in range(N)]
ans = [0, 0]

visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i, j, [picture[i][j]])
            cnt += 1
ans[0] = cnt

visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if picture[i][j] in ['R', 'G']:
                dfs(i, j, ['R', 'G'])
            else:
                dfs(i, j, ['B'])
            cnt += 1

ans[1] = cnt

print(*ans)
