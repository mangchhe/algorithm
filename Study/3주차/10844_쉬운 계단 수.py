import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    res = 0

    dp = [[0] * 10 for _ in range(n)]

    for i in range(1, 10):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])

    for i in range(10):
        res += dp[n - 1][i]

    print(res % 10**9)
