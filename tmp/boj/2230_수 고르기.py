input = __import__('sys').stdin.readline

N, M = map(int, input().split())
arr = sorted(int(input()) for _ in range(N))
ans = float('INF')

if N == 1:
    print(0)
    exit()

l, r = 0, 1

while l < N and r < N:
    if arr[r] - arr[l] >= M and r - l > 1:
        ans = min(ans, arr[r] - arr[l])
        l += 1
    elif arr[r] - arr[l] >= M:
        ans = min(ans, arr[r] - arr[l])
        l += 1
    else:
        r += 1

print(ans)
