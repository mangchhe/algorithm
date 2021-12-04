n = int(input())
dp = [1, 3, 5]

for i in range(2, n):
    dp.append((dp[-1] + dp[-2] * 2) % 10007)

print(dp[n - 1])
