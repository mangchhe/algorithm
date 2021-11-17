N = int(input())
wire = sorted(list(map(int, input().split())) for _ in range(N))
dp = [1] * len(wire)

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if wire[i][1] > wire[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
