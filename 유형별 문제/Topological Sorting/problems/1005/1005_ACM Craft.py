from collections import defaultdict, deque

input = __import__("sys").stdin.readline


def solve():
    q = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            ans[i] = delay[i]
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            ans[i] = max(ans[i], ans[now] + delay[i])
            if indegree[i] == 0:
                q.append(i)


for _ in range(int(input())):
    N, K = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    indegree = [0] * (N + 1)
    graph = defaultdict(list)
    ans = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(input())
    solve()
    print(ans[W])
