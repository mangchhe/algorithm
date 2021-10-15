# https://www.acmicpc.net/problem/16507

input = __import__('sys').stdin.readline

R, C, Q = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(R)]
dp = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        dp[i][j] = pixels[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    print((dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]) // ((x2 - x1 + 1) * (y2 - y1 + 1)))
