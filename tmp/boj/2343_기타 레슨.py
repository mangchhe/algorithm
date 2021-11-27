def make_disk(arr, size):
    total = 1
    spare = size
    idx = 0
    while idx < len(arr):
        if arr[idx] > size:
            total = float('INF')
            break
        if spare - arr[idx] >= 0:
            spare -= arr[idx]
            idx += 1
        else:
            total += 1
            spare = size
    return total

N, M = map(int, input().split())
length = list(map(int, input().split()))

l, r = 1, sum(length)
while l <= r:
    mid = (l + r) // 2
    if make_disk(length, mid) > M:
        l = mid + 1
    else:
        r = mid - 1

print(l)
