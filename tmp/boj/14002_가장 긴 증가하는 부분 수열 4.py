N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
bt = [-1] * N

for i in range(1, N):
    idx = -1
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = max(dp[i], dp[j] + 1)
                idx = j
    if idx != -1:
        bt[i] = idx
            
maxVal = max(dp)
now = 0
for idx, val in enumerate(dp):
    if maxVal == val:
        now = idx
        break

ans = [arr[now]]
while bt[now] != -1:
    ans.append(arr[bt[now]])
    now = bt[now]

print(len(ans))
print(*reversed(ans))
