N, M, L = map(int, input().split())
pos = [0] + sorted(map(int, input().split())) + [L]
res = 0

l, r = 1, L

while l <= r:
    mid = (l + r) // 2
    cnt = 0
    for i in range(len(pos) - 1):
        cnt += (pos[i + 1] - pos[i] - 1) // mid

    if cnt <= M:
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)
