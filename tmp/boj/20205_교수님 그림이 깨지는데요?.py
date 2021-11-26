def coloring(arr, x, y):
    for i in range(x, x + K):
        for j in range(y, y + K):
            arr[i][j] = 1


N, K = map(int, input().split())
arr = [input().split() for _ in range(N)]
ans = [[0] * (N * K) for _ in range(N * K)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            coloring(ans, i * K, j * K)

for a in ans:
    print(*a)
