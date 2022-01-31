N = int(input())
box = list(map(int, input().split()))
dp = [1] * N
ans = 1

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])

print(ans)
