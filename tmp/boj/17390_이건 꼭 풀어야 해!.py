# https://www.acmicpc.net/problem/17390

input = __import__('sys').stdin.readline

N, Q = map(int, input().split())
nList = list(map(int, input().split()))
nList = sorted(nList)
dp = [0]

for i in range(len(nList)):
    dp.append(dp[i] + nList[i])

for _ in range(Q):
    L, R = map(int, input().split())
    print(dp[R] - dp[L - 1])
