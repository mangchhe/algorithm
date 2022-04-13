N = int(input())
liquid = list(map(int, input().split()))
_min = float('INF')
ans = [0, 0]

l = 0
r = N - 1
while l < r:
    diff = liquid[l] + liquid[r]
    if abs(diff) < _min:
        _min = abs(diff)
        ans = [liquid[l], liquid[r]]
    
    if diff > 0:
        r -= 1
    elif diff < 0:
        l += 1
    else:
        break

print(*ans)
