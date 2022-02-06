def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def dfs(x, y, cnt, sumValue):
    global ans
    if cnt == K:
        ans = max(ans, sumValue)
        return
    
    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            if visited[i][j]:
                continue
            for cx, cy in move(i, j):
                if -1 < cx < N and -1 < cy < M:
                    if visited[cx][cy]:
                        break
            else:
                visited[i][j] = 1
                dfs(i, j, cnt + 1, sumValue + board[i][j])
                visited[i][j] = 0

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = -float('INF')

dfs(0, 0, 0, 0)

print(ans)
