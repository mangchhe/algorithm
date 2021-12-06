n, k = map(int, input().split())
moneys = sorted(int(input()) for _ in range(n))
dp = [0] * (k + 1)
dp[0] = 1

for money in moneys:
    for j in range(money, k + 1):
        dp[j] = dp[j - money] + dp[j]

print(dp[k])
