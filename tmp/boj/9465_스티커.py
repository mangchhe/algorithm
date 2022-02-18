input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(3)]

    dp[1][0] = sticker[0][0]
    dp[2][0] = sticker[1][0]

    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = max(dp[0][i - 1], dp[2][i - 1]) + sticker[0][i]
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1]) + sticker[1][i]

    print(max(dp[0][N - 1], dp[1][N - 1], dp[2][N - 1]))
