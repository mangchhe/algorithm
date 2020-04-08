from sys import stdin
from collections import deque

x = [-1, 1, 0, 0]
y = [0, 0, -1 ,1]

m, n = map(int, input().split())

mapList = []

def bfs(node_x, node_y):

    global mapList

    visited = [[0 for i in range(n)] for j in range(m)]
    visited[node_x][node_y] = 1
    queue = deque([(node_x, node_y)])

    while queue:

        node_x, node_y = queue.popleft()

        for i in range(4):

            if (node_x + x[i] > -1 and node_x + x[i] < m) and (node_y + y[i] > -1 and node_y + y[i] < n) and mapList[node_x + x[i]][node_y + y[i]] == 1 and visited[node_x + x[i]][node_y + y[i]] == 0:

                mapList[node_x + x[i]][node_y + y[i]] = mapList[node_x][node_y] + 1

                queue.append((node_x + x[i], node_y + y[i]))

    return mapList[m - 1][n - 1]

if __name__ == '__main__':

    for _ in range(m):

        mapList.append(list(map(int, stdin.readline().strip())))

    print(bfs(0,0))