def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

N = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
indexs = []

for val in arr:
    if dp[-1] < val:
        indexs.append(len(dp))
        dp.append(val)
    else:
        idx = binary_search(dp, val)
        dp[idx] = val
        indexs.append(idx)

cnt = len(dp) - 1
ans = []
for i in range(len(arr)-1, -1, -1):
    if cnt == indexs[i]:
        ans.append(arr[i])
        cnt -= 1

    if cnt == -1:
        break

print(len(ans))
print(*reversed(ans))
