import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    dp = [float('INF')] * (n + 1)
    dp[n] = 0

    for i in range(n, 1, -1):
        dp[i - 1] = min(dp[i] + 1, dp[i - 1])
        if i % 3 == 0:
            dp[i // 3] = min(dp[i] + 1, dp[i // 3])
        if i % 2 == 0:
            dp[i // 2] = min(dp[i] + 1, dp[i // 2])

    print(dp[1])