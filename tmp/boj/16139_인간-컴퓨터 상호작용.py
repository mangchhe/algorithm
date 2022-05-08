import sys
input = sys.stdin.readline
print = sys.stdout.write

s = input().rstrip()
dp = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(len(s)):
    for j in range(26):
        dp[i + 1][j] = dp[i][j]
    _ascii = ord(s[i]) - 97
    dp[i + 1][_ascii] = dp[i][_ascii] + 1

N = int(input())

for _ in range(N):
    c, s, e = input().split()
    s, e = int(s), int(e)
    _ascii = ord(c) - 97
    print(str(dp[e + 1][_ascii] - dp[s][_ascii]) + '\n')
