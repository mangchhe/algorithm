# https://www.acmicpc.net/problem/11660

input = __import__('sys').stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = matrix[0][0]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]

for _ in range(M):
    s1, e1, s2, e2 = map(int, input().split())
    s1, e1, s2, e2 = s1, e1, s2, e2
    print(dp[s2][e2] - dp[s1 - 1][e2] - dp[s2][e1 - 1] + dp[s1 - 1][e1 - 1])
