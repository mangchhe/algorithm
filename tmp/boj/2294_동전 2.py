N, K = map(int, input().split())
moneys = sorted(int(input()) for _ in range(N))
dp = [float('INF')] * (K + 1)
dp[0] = 0

for money in moneys:
    for i in range(money, K + 1):
        dp[i] = min(dp[i - money] + 1, dp[i])

print(-1 if dp[K] == float('INF') else dp[K])
