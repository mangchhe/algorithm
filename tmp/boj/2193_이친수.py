# https://www.acmicpc.net/problem/2193

# 1
# 10
# 100, 101
# 1000, 1010, 1001
# 10100, 10101, 10000, 10010, 10001

N = int(input())
dp = [0, 1]

if N > 1:
    for i in range(2, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])

print(dp[N])
