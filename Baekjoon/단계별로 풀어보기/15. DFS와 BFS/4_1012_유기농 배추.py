from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

visited = []
graph = []

def solve(start_node_X, start_node_Y):
    global visited
    global graph

    visited[start_node_X][start_node_Y] = 1

    if start_node_X - 1 > -1 and visited[start_node_X - 1][start_node_Y] == 0 and graph[start_node_X - 1][start_node_Y] == 1:
        solve(start_node_X - 1,start_node_Y)
    try:
        if visited[start_node_X + 1][start_node_Y] == 0 and graph[start_node_X + 1][start_node_Y] == 1:
            solve(start_node_X + 1,start_node_Y)
    except:
        pass
    if start_node_Y - 1 > -1 and visited[start_node_X][start_node_Y - 1] == 0 and graph[start_node_X][start_node_Y - 1] == 1:
        solve(start_node_X,start_node_Y - 1)
    try:
        if visited[start_node_X][start_node_Y + 1] == 0 and graph[start_node_X][start_node_Y + 1] == 1:
            solve(start_node_X,start_node_Y + 1)
    except:
        pass


for _ in range(int(input())):
    row, column, n = map(int,stdin.readline().split())
    visited = [[0 for val in range(row)] for val in range(column)]
    graph = [[0 for val in range(row)] for val in range(column)]
    count = 0

    for _ in range(n):
        M, N = map(int, stdin.readline().split())
        graph[N][M] = 1

    for i in range(column):
        for j in range(row):
            if visited[i][j] != 1 and graph[i][j] == 1:
                solve(i,j)
                count += 1

    print(count)