N = int(input())
arr = list(map(int, input().split()))
fdp = [1] * N
rdp = [1] * N
ans = 0

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            fdp[i] = max(fdp[i], fdp[j] + 1)

for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            rdp[i] = max(rdp[i], rdp[j] + 1)

for i in zip(fdp, rdp):
    ans = max(ans, sum(i))

print(ans - 1)
