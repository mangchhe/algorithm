import sys

input = sys.stdin.readline

if __name__ == '__main__':

    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = data[0][0]

    for k in range(n - 1):
        for i in range(k + 1):
            for j in range(i, i + 2):
                if dp[k][i] + data[k + 1][j] > dp[k + 1][j]:
                    dp[k + 1][j] = dp[k][i] + data[k + 1][j]

    print(max(dp[n - 1]))