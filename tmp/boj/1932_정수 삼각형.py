input = __import__('sys').stdin.readline

N = int(input())
arr = [list(map(int,  input().split())) for _ in range(N)]
dp = [[0] * (1 + i) for i in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i - 1][0]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(arr[i][j] + dp[i - 1][j - 1], arr[i][j] + dp[i - 1][j])

print(max(dp[N - 1]))
