from sys import stdin
from collections import deque

box = []
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
M = 0
N = 0

def bfs(start_node):

    going_node = deque(start_node)
    visited = [[0 for i in range(M)] for j in range(N)]

    while going_node:

        x_node, y_node = going_node.popleft()

        for i in range(4):

            x_pos = x_node + x[i]
            y_pos = y_node + y[i]

            if x_pos > -1 and x_pos < N and y_pos > -1 and y_pos < M and visited[x_pos][y_pos] == 0 and box[x_pos][y_pos] == 0:

                visited[x_pos][y_pos] = 1
                going_node.append((x_pos,y_pos))
                box[x_pos][y_pos] = box[x_node][y_node] + 1

if __name__ == '__main__':

    M, N = map(int, input().split())

    for _ in range(N):
        box.append(list(map(int, stdin.readline().strip().split())))

    one_repos = []

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                one_repos.append((i,j))

    bfs(one_repos)

    tmp = []
    for val in box:
        tmp.extend(val)

    if all(tmp):
        print(max(tmp) - 1)
    else:
        print(-1)