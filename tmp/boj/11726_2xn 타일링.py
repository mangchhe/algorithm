# https://www.acmicpc.net/problem/11726

N = int(input())

dp = [0, 1, 2, 3]

if N < 4:
    print(dp[N])
else:
    for i in range(4, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    print(dp[N] % 10007)
