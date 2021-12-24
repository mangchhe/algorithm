from collections import deque
input = __import__('sys').stdin.readline

def solve():
    q = deque([])
    
    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)
            ans.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
                ans.append(i)

N, M = map(int, input().split())
ans = []
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    _, *singer = map(int, input().split())
    if len(singer) > 1:
        for i in range(1, len(singer)):
            indegree[singer[i]] += 1
            graph[singer[i - 1]].append(singer[i])

solve()

if len(ans) == N:
    for i in ans: print(i)
else:
    print(0)
