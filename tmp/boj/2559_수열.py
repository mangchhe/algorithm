# 투 포인터

N, K = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = K - 1
_sum = sum(arr[:K])
ans = _sum

while r < N - 1:
    _sum = _sum - arr[l] + arr[r + 1]
    ans = max(ans, _sum)
    l += 1
    r += 1

print(ans)

# 누적합

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = -float('INF')
dp = [0]

for i in range(N):
    dp.append(dp[i] + arr[i])

for i in range(K, N + 1):
    ans = max(ans, dp[i] - dp[i - K])

print(ans)
