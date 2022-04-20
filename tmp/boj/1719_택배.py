input = __import__('sys').stdin.readline

N, M = map(int, input().split())
graph = [[float('INF')] * (N + 1) for _ in range(N + 1)]
ans = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    graph[i][i] = 0
    ans[i][i] = '-'

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost
    ans[a][b] = b
    ans[b][a] = a

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                ans[i][j] = ans[i][k]

for i in range(1, len(ans)):
    print(*ans[i][1:])
