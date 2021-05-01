def solution(m, n, puddles):
    answer = 0
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for puddle in puddles:
        x, y = puddle
        dp[y][x] = -1

    dp[0][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
