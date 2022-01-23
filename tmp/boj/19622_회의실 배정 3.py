input = __import__('sys').stdin.readline

N = int(input())
sessions = [tuple(map(int, input().split())) for _ in range(N)] + [(0, 0, 0)]
dp = [[0] * 2 for _ in range(100001)]

dp[0][1] = dp[1][0] = sessions[0][2]
dp[1][1] = sessions[1][2]

for i in range(2, N):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = sessions[i][2] + dp[i - 1][0]

print(max(dp[N - 1][0], dp[N - 1][1]))
