import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[float('INF')] * 3 for i in range(n)]
    for i in range(3):
        dp[0][i] = data[0][i]

    for k in range(n - 1):
        for i in range(3):
            for j in range(3):
                if j == i:
                    continue
                else:
                    if dp[k][i] + data[k + 1][j] < dp[k + 1][j]:
                        dp[k + 1][j] = dp[k][i] + data[k + 1][j]
    print(min(dp[n - 1]))