def bellman(start):
    distance[start] = 0

    for i in range(N):
        for j in range(M):
            cur = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]

            if distance[cur] != float('INF') and distance[cur] + cost < distance[next_node]:
                distance[next_node] = distance[cur] + cost

                if i == N - 1:
                    return 0

    return 1

N, M = map(int, input().split())
graph = []
distance = [float('INF')] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

if bellman(1):
    for ans in distance[2:]:
        if ans == float('INF'):
            print(-1)
        else:
            print(ans)
else:
    print(-1)

