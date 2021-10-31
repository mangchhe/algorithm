# https://www.acmicpc.net/problem/1913

N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]

r, c = -1, 0
inc = 1
cnt = N ** 2

while N > 0:

    for _ in range(N):
        r += inc
        arr[r][c] = cnt
        cnt -= 1

    N -= 1

    for _ in range(N):
        c += inc
        arr[r][c] = cnt
        cnt -= 1

    inc *= -1

for i in range(len(arr)):
    print(*arr[i])

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == M:
            print(i + 1, j + 1)
            exit()
