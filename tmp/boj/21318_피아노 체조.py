input = __import__('sys').stdin.readline

N = int(input())
difficult = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(2, N + 1):
    if difficult[i] < difficult[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[e] - dp[s])