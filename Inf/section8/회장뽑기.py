import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    dp = [[float('INF')] * (n + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    while True:
        x, y = map(int, input().split())
        if x == -1 and y == -1:
            break
        dp[x][y] = 1
        dp[y][x] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

    res = [0] * (n + 1)
    score = 100
    for i in range(1, n + 1):
        minVal = float('INF')
        for j in range(1, n + 1):
            res[i] = max(res[i], dp[i][j])
        score = min(score, res[i])
    out = []
    for i in range(1, n + 1):
        if res[i] == score:
            out.append(i)
    print("%d %d" % (score, len(out)))
    for o in out:
        print(o, end=' ')