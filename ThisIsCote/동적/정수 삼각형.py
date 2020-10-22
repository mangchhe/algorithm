"""
    작성일 : 20/10/22
"""

import sys

input = sys.stdin.readline
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
dp = [[0] * i for i in range(1, n + 1)]
dp[0][0] = data[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][0] = data[i][0] + dp[i - 1][0]
        elif j < i:
            if dp[i - 1][j - 1] + data[i][j] > dp[i][j]:
                dp[i][j] = dp[i - 1][j - 1] + data[i][j]
            if dp[i - 1][j] + data[i][j] > dp[i][j]:
                dp[i][j] = dp[i - 1][j] + data[i][j]                
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + data[i][j]

print(max(dp[n - 1]))