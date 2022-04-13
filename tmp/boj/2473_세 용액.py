N = int(input())
liquid = sorted(map(int, input().split()))
_min = float('INF')
ans = [0, 0, 0]

for i in range(N):
    l = i + 1
    r = N - 1
    flag = False
    while l < r:
        diff = liquid[i] + liquid[l] + liquid[r]
        if abs(diff) < _min:
            _min = abs(diff)
            ans = [liquid[i], liquid[l], liquid[r]]

        if diff < 0:
            l += 1
        elif diff > 0:
            r -= 1
        else:
            flag = True
            break
    if flag:
        break

print(*ans)
