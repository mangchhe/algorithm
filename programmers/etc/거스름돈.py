def solution(n, money):

    dp = [0] * (n + 1)
    dp[0] = 1

    for m in money:
        for i in range(m, n + 1):
            dp[i] = (dp[i] + dp[i - m]) % 1000000007

    return dp[n] % 1000000007


print(soluton(5, [1, 2, 5]))
