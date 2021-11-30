N = int(input())
dp = [0, 1]

for i in range(2, N + 1):
    dp.append((dp[-1] + dp[-2]) % 1000000007)

print(dp[N])
