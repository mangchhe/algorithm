input = __import__('sys').stdin.readline

N, M = map(int, input().split())
jealousy = [int(input()) for _ in range(M)]

l, r = 1, max(jealousy)
ans = float('INF')

while l <= r:
    mid = (l + r) // 2
    total = 0
    for i in jealousy:
        total += i // mid + 1 if i % mid != 0 else i // mid
    if N >= total:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1

print(ans)
