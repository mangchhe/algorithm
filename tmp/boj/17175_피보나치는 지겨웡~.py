N = int(input())

dp = [1, 1]

for i in range(2, N + 1):
    dp.append((dp[i - 2] + dp[i - 1] + 1) % (int(1e9) + 7))

print(dp[N] % 10000000007)
