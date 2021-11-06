N = int(input())
coins = [1, 2, 5, 7]
dp = [float('INF')] * (N + 1)
dp[0] = 0

for i in range(4):
    for j in range(N - coins[i] + 1):
        dp[j + coins[i]] = min(dp[j] + 1, dp[j + coins[i]])

print(dp[N])
