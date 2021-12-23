from collections import deque

input = __import__('sys').stdin.readline

def solve():
    q = deque([])

    for i in range(N):
        if not indegree[i]:
            q.append(i)
    while q:
        n = q.popleft()
        for i in route[n]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[n] + dis[i])
            if not indegree[i]:
                q.append(i)

N = int(input())
indegree = [0] * N
dp = [0] * N
dis = [0] * N
route = [[] for _ in range(N)]

for i in range(N):
    v = list(map(int, input().split()))
    dis[i] = v[0]
    dp[i] = v[0]
    for j in range(1, len(v) - 1):
        indegree[i] += 1
        route[v[j] - 1].append(i)

solve()

for i in dp:
    print(i)
