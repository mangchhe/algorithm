import sys

# sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):

    if x == n - 1 and y == n - 1:
        return
    else:
        for i in range(2):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1 < tx < n and -1 < ty < n:
                if dp[tx][ty] > dp[x][y] + data[tx][ty]:
                    dp[tx][ty] = dp[x][y] + data[tx][ty]
                    dfs(tx, ty)


if __name__ == '__main__':

    n = int(input())
    data = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[float('INF')] * n for _ in range(n)]
    dp[0][0] = data[0][0]

    dfs(0, 0)

    print(dp[n - 1][n - 1])