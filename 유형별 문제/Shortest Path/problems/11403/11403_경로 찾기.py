N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 0:
            graph[i][j] = float('INF')


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for g in graph:
    print(' '.join(map(lambda x: str(0) if x == float('INF') else str(1), g)))