from sys import stdin
from collections import deque

x = [-1, 1, 0, 0]
y = [0, 0, -1 ,1]
h = [0, -1, 1]

M, N, H = map(int, input().split())

box = []

for i in range(H):
   box.append([])
   for j in range(N):
       box[i].append(list(map(int, stdin.readline().strip().split())))

def dfs(start_node):
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    queue = deque(start_node)

    while queue:
        node_h, node_x, node_y = queue.popleft()

        for i in h:
            if node_h + i > -1 and node_h + i < H and visited[node_h + i][node_x][node_y] == 0 and box[node_h + i][node_x][node_y] == 0:
                visited[node_h + i][node_x][node_y] = 1
                if box[node_h][node_x][node_y] == 1:
                    box[node_h + i][node_x][node_y] = box[node_h][node_x][node_y]
                else:
                    box[node_h + i][node_x][node_y] = box[node_h][node_x][node_y]+1
                queue.append((node_h + i, node_x, node_y))

            if node_h + i > -1 and node_h + i < H:
                for j, k in zip(x, y):
                    if node_x + j > -1 and node_x + j < N and node_y + k > -1 and node_y + k < M and visited[node_h][node_x+j][node_y+k] == 0 and box[node_h+i][node_x+j][node_y+k] == 0:
                        visited[node_h][node_x + j][node_y + k] = 1
                        box[node_h][node_x + j][node_y + k] = box[node_h][node_x][node_y] + 1
                        queue.append((node_h,node_x + j,node_y + k))

if __name__ == '__main__':

    one_respo = []

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    one_respo.append((i,j,k))

    dfs(one_respo)

    tmp = [k for i in box for j in i for k in j]
    if all(tmp):
            print(max(tmp) - 1)
    else:
        print(-1)
