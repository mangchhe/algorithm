N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue

        dis = board[i][j]
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < N:
            dp[i][board[i][j] + j] += dp[i][j]

print(dp[N - 1][N - 1])
