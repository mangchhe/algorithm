def traverse(n, s, l, t):
    global ans
    if L <= t <= R and l - s >= X:
        ans += 1
    if n >= N or t > R:
        return

    for i in range(n, N):
        if s == 0 and l == 0:
            traverse(i + 1, arr[i], arr[i], t + arr[i])
        elif arr[i] < s:
            traverse(i + 1, arr[i], l, t + arr[i])
        elif arr[i] > l:
            traverse(i + 1, s, arr[i], t + arr[i])
        else:
            traverse(i + 1, s, l, t + arr[i])

N, L, R, X = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0] * N
ans = 0

traverse(0, 0, 0, 0)

print(ans)