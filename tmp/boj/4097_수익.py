input = __import__('sys').stdin.readline

while True:
    N = int(input())
    if N == 0:
        break
    dp = [int(input()) for _ in range(N)]

    for i in range(1, N):
        if dp[i] + dp[i - 1] > dp[i]:
            dp[i] = dp[i] + dp[i - 1]

    print(max(dp))
