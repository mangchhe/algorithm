from collections import defaultdict, deque

input = __import__("sys").stdin.readline


def solve():
    q = deque([])

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

solve()
