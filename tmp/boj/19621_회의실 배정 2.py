N = int(input())
dp = [0] * N
time = []
for _ in range(N): 
    time.append(list(map(int, input().split())))

dp[0] = time[0][2]

if N > 1:
    dp[1] = time[1][2]

for i in range(2, N):
    maxVal = dp[i - 1]
    for j in range(i - 2, -1, -1):
        maxVal = max(maxVal, dp[j] + time[i][2])
    dp[i] = maxVal

print(max(dp))
