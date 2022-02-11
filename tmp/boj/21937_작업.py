import sys

input = sys.stdin.readline

# 방법1
# 재귀함수
sys.setrecursionlimit(10 ** 6)

def dfs(n):
    global ans
    ans += 1
    for i in indegree[n]:
        if i not in visited:
            visited.add(i)
            dfs(i)

N, M = map(int, input().split())
indegree = [[] for _ in range(N + 1)]
visited = set()
ans = -1

for _ in range(M):
    a, b = map(int, input().split())
    indegree[b].append(a)

dfs(int(input()))

print(ans)

# 방법 2
# 스택
N, M = map(int, input().split())
visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

K = int(input())
q = [K]
visited[K] = 1
ans = 0

while q:
    now = q.pop()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
            ans += 1

print(ans)
