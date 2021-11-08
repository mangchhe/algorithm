N = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

for i in range(1, N):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], arr[i] + dp[j])

print(max(dp))
