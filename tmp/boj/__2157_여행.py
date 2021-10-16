# https://www.acmicpc.net/problem/2157

N, M, K = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(K)]
routeDic = {}

for i in range(len(routes)):
    s, e, w = routes[i]
    if s > e:
        continue
    if not routeDic.get(s):
        routeDic[s] = [(e, w)]
    else:
        routeDic[s].append((e, w))

dp = [[0] * 301 for _ in range(301)]

for i in range(len(routeDic[1])):
    next = routeDic[1][i][0]
    weight = routeDic[1][i][1]
    dp[next][2] = max(dp[next][2], weight)

for i in range(2, M):
    for j in range(1, N + 1):
        if dp[j][i] != 0 and routeDic.get(j):
            for k in routeDic[j]:
                dp[k[0]][i + 1] = max(dp[k[0]][i + 1], dp[j][i] + k[1])

ans = 0

for i in range(M + 1):
    ans = max(ans, dp[N][i])

print(ans)
