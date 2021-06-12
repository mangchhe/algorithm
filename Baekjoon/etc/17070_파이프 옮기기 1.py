import sys

input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

# 방법 1(DFS)

# res = 0
# def dfs(x, y, d):
#     global res
#     if x == N - 1 and y == N - 1:
#         res += 1
#         return

#     if d == -1:
#         if y + 1 < N and map[x][y + 1] == 0:
#             dfs(x, y + 1, -1)
#         if x + 1 < N and y + 1 < N:
#             if map[x + 1][y] == 0 and map[x][y + 1] == 0 and map[x + 1][y + 1] == 0:
#                 dfs(x + 1, y + 1, 0)
#     elif d == 0:
#         if y + 1 < N and map[x][y + 1] == 0:
#             dfs(x, y + 1, -1)
#         if x + 1 < N and y + 1 < N:
#             if map[x + 1][y] == 0 and map[x][y + 1] == 0 and map[x + 1][y + 1] == 0:
#                 dfs(x + 1, y + 1, 0)
#         if x + 1 < N and map[x + 1][y] == 0:
#             dfs(x + 1, y, 1)
#     else:
#         if x + 1 < N and map[x + 1][y] == 0:
#             dfs(x + 1, y, 1)
#         if x + 1 < N and y + 1 < N:
#             if map[x + 1][y] == 0 and map[x][y + 1] == 0 and map[x + 1][y + 1] == 0:
#                 dfs(x + 1, y + 1, 0)


# dfs(0, 1, -1)

# print(res)

# 방법 2(Dynamic)

dp = [[[0] * N for _ in range(N)] for _ in range(3)]

for i in range(1, N):
    if map[0][i] == 0:
        dp[0][0][i] = 1
    else:
        break

for i in range(1, N):
    for j in range(2, N):
        if map[i][j] == 0 and map[i - 1][j] == 0 and map[i][j - 1] == 0:
            dp[2][i][j] = (
                dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
            )
        if map[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(dp[0][N - 1][N - 1] + dp[1][N - 1][N - 1] + dp[2][N - 1][N - 1])
