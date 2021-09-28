# https://www.acmicpc.net/problem/14500

# 방법 1

input = __import__('sys').stdin.readline

def dfs(x, y, total, cnt):
    global ans
    if cnt == 4:
        ans = max(ans, total)
        return
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if -1 < cx < N and -1 < cy < M and not visited[cx][cy]:
            visited[cx][cy] = 1
            dfs(cx, cy, total + paper[cx][cy], cnt + 1)
            visited[cx][cy] = 0

def bfs(x, y):
    res = 0
    for i in range(4):
        total = paper[x][y]
        for j in range(4):
            if j == i:
                continue
            cx = x + dx[j]
            cy = y + dy[j]
            if -1 < cx < N and -1 < cy < M:
                total += paper[cx][cy]
            else:
                break
        else:
            res = max(res, total)
    return res

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, paper[i][j], 1)
        visited[i][j] = 0
        ans = max(ans, bfs(i, j))

print(ans)
