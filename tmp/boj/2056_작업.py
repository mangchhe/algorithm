from collections import deque

# 정석 
# def solve():
#     q = deque([])
#     for i in range(1, N + 1):
#         if not indegree[i]:
#             q.append(i)
#     while q:
#         n = q.popleft()
#         for i in graph[n]:
#             dp[i] = max(dp[i], dp[n] + dis[i])
#             indegree[i] -= 1
#             if not indegree[i]:
#                 q.append(i)

# N = int(input())

# dis = [0] * (N + 1)
# indegree = [0] * (N + 1)
# dp = [0] * (N + 1)
# graph = [[] for _ in range(N + 1)]

# for i in range(1, N + 1):
#     v = list(map(int, input().split()))
#     dis[i] = v[0]
#     dp[i] = v[0]
#     for j in range(2, len(v)):
#         graph[v[j]].append(i)
#         indegree[i] += 1

# solve()

# print(max(dp))

# 개선 방법
# K번 째 작업이 1 ~ K - 1 의 작업들로만 선행 관계를 가지기 때문에 가능
input = __import__('sys').stdin.readline

N = int(input())
ans = 0
times = [0] * (N + 1)

for i in range(1, N + 1):
    time, *indegree = map(int, input().split())
    times[i] = time
    if len(indegree) > 1:
        times[i] = time + max(map(lambda x: times[x], indegree[1:]))

    ans = max(ans, times[i])

print(ans)
