input = __import__("sys").stdin.readline

for _ in range(int(input())):
    input()
    money = list(map(int, input().split()))
    M = int(input())
    dp = [0] * (M + 1)
    dp[0] = 1

    for m in money:
        for i in range(m, M + 1):
            dp[i] += dp[i - m]

    print(dp[M])
