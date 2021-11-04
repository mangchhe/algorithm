input = __import__('sys').stdin.readline

for _ in range(int(input())):
    N = int(input())
    moneys = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(N):
        for j in range(moneys[i], target + 1):
            dp[j] += dp[j - moneys[i]]

    print(dp[target])
    
