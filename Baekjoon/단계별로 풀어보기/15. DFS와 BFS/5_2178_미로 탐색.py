from collections import deque

miro = []
graph = {}

def dfs(start_node):

    global graph
    visited = []
    stack = deque([start_node])

    while stack:

        M, N = stack.popleft()

        if (M,N) not in visited:
            visited.append((M,N))
            stack.extendleft(graph[(M,N)][::-1])

    return visited

def create_graph():
    global miro
    global graph
    visited = [[0 for i in range(N)] for j in range(M)]
    print(M,N)
    for i in range(M):
        for j in range(N):
            if miro[i][j] == 1:
                if i - 1 > -1 and visited[i - 1][j] == 0 and miro[i - 1][j] == 1:
                    visited[i - 1][j] = 1
                    if (i,j) not in graph:
                        graph[(i,j)] = [(i-1,j)]
                    else:
                        if (i-1,j) not in graph[(i,j)]:
                            graph[(i,j)].append((i-1,j))
                    if (i-1,j) not in graph:
                        graph[(i-1,j)] = [(i,j)]
                    else:
                        if (i,j) not in graph[(i-1,j)]:
                            graph[(i-1,j)].append((i,j))
                if i + 1 < M and visited[i + 1][j] == 0 and miro[i + 1][j] == 1:
                    visited[i + 1][j] = 1
                    if (i,j) not in graph:
                        graph[(i,j)] = [(i+1,j)]
                    else:
                        if (i+1,j) not in graph[(i,j)]:
                            graph[(i,j)].append((i+1,j))
                    if (i+1,j) not in graph:
                        graph[(i+1,j)] = [(i,j)]
                    else:
                        if (i,j) not in graph[(i+1,j)]:
                            graph[(i+1,j)].append((i,j))
                if j - 1 > - 1 and visited[i][j - 1] == 0 and miro[i][j - 1] == 1:
                    visited[i][j - 1] = 1
                    if (i,j) not in graph:
                        graph[(i,j)] = [(i,j-1)]
                    else:
                        if (i,j-1) not in graph[(i,j)]:
                            graph[(i,j)].append((i,j-1))
                    if (i,j-1) not in graph:
                        graph[(i,j-1)] = [(i,j)]
                    else:
                        if (i,j) not in graph[(i,j-1)]:
                            graph[(i,j-1)].append((i,j))
                if j + 1 < M and visited[i][j + 1] == 0 and miro[i][j + 1] == 1:
                    visited[i][j + 1] = 1
                    if (i,j) not in graph:
                        graph[(i,j)] = [(i,j+1)]
                    else:
                        if (i,j+1) not in graph[(i,j)]:
                            graph[(i,j)].append((i,j+1))
                    if (i,j+1) not in graph:
                        graph[(i+1,j)] = [(i,j)]
                    else:
                        if (i,j) not in graph[(i,j+1)]:
                            graph[(i+1,j)].append((i,j))

if __name__ == '__main__':

    M, N = map(int, input().split())

    for _ in range(M):
        miro.append(list(map(int, list(input()))))

    create_graph()
    print(dfs((0,0)))