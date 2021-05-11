def solve(n, graph):

    res = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == float('INF'):
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        graph[i][j] = 1
                    if graph[i][k] == -1 and graph[k][j] == -1:
                        graph[i][j] = -1

    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == float('INF'):
                break
        else:
            res += 1

    return res


def solution(n, results):

    graph = [[float('INF')] * n for i in range(n)]

    for result in results:
        graph[result[0] - 1][result[1] - 1] = 1
        graph[result[1] - 1][result[0] - 1] = -1

    return solve(n, graph)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))