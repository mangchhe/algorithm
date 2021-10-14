# https://www.acmicpc.net/problem/16401

M, N = map(int, input().split())
snacks = sorted(map(int, input().split()), reverse = True)
ans = 0

l, r = 1, snacks[0]

while l <= r:
    mid = (l + r) // 2
    total = 0
    for s in snacks:
        if s >= mid:
            total += s // mid
        else:
            break

    if total >= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
