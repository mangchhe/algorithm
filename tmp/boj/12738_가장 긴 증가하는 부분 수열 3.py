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

for a in arr:
    if a > dp[-1]:
        dp.append(a)
    else:
        dp[binary_search(dp, a)] = a

print(len(dp))

