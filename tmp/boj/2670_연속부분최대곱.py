# https://www.acmicpc.net/problem/2670

# 방법1
# O(N^2)

N = int(input())
nList = [float(input()) for _ in range(N)]
ans = 0

for i in range(len(nList)):
    total = 1
    for j in range(i, len(nList)):
        total *= nList[j]
        ans = max(ans, total)

print('%.3f' % ans)

# 방법2

N = int(input())
nList = [float(input()) for _ in range(N)]
dp = [0]

for n in nList:
    dp.append(n)

for i in range(1, len(dp)):
    dp[i] = max(dp[i], dp[i] * dp[i - 1])

print('%.3f' % max(dp))
