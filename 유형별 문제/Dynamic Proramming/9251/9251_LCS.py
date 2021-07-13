input = __import__("sys").stdin.readline

s1 = "0" + input().rstrip()
s2 = "0" + input().rstrip()

dp = [[0] * (len(s2)) for _ in range(len(s1))]
ans = 0

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(ans)
