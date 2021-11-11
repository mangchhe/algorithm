N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = float('INF')

for i in range(N):
    tmp = [0] * N
    tmp[i] = arr[i]
    for j in range(i):
        tmp[i - j - 1] = arr[i] - (K * (j + 1))
    for j in range(N - i - 1):
        tmp[i + j + 1] = arr[i] + (K * (j + 1))

    total = 0

    if tmp[0] < 1:
        continue

    for j in range(N):
        if arr[j] != tmp[j]:
            total += 1

    ans = min(ans, total)

print(ans)
