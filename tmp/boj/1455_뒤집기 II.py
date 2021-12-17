N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
ans = 0

for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if arr[i][j] == 1:
            for x in range(0, i + 1):
                for y in range(0, j + 1):
                    arr[x][y] ^= 1
            ans += 1

print(ans)
