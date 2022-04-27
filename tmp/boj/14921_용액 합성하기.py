N = int(input())
liquid = list(map(int, input().split()))
ans = float('inf')

l, r = 0, N - 1
while l < r:
    _sum = liquid[l] + liquid[r]
    if abs(ans) > abs(_sum):
        ans = _sum

    if  _sum < 0:
        l += 1
    else:
        r -= 1

print(ans)
