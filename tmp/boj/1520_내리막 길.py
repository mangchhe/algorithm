__import__('sys').setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def traverse(x, y):
    global ans
    if x == N - 1 and y == M - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0

    for cx, cy in move(x, y):
        if cx < 0 or cx > N - 1 or cy < 0 or cy > M - 1:
            continue
        if arr[cx][cy] < arr[x][y]:
            dp[x][y] += traverse(cx, cy)

    return dp[x][y]

print(traverse(0, 0))

