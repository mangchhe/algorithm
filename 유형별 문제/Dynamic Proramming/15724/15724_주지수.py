input = __import__("sys").stdin.readline
MI = lambda: map(int, input().split())

N, M = map(int, input().split())

land = [list(MI()) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = land[0][0]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[0][j] = dp[0][j - 1] + land[0][j]
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + land[i][0]
        else:
            dp[i][j] = land[i][j] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

for _ in range(int(input())):
    s, e, ss, ee = MI()
    s, e, ss, ee = s - 1, e - 1, ss - 1, ee - 1
    a, b, c = 0, 0, 0
    if s - 1 > -1 and e - 1 > -1:
        a = dp[s - 1][e - 1]
    if s - 1 > -1:
        b = dp[s - 1][ee]
    if e - 1 > -1:
        c = dp[ss][e - 1]

    print(dp[ss][ee] - b - c + a)
