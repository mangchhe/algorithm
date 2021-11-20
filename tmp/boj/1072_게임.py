X, Y = map(int, input().split())
mod = Y * 100 // X
ans = float('INF')

l, r = 1, X

while l <= r:
    mid = (l + r) // 2
    
    if (Y + mid) * 100 // (X + mid) > mod:
        ans = min(ans, mid)
        r = mid - 1
    else:
        l = mid + 1

if ans == float('INF'):
    print(-1)
else:
    print(ans)
