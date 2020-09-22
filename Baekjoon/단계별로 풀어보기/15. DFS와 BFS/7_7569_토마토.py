"""
    수정일 : 20/09/22 - 시간초과
"""

""" 
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
"""

from sys import stdin
from collections import deque

def solve(oneNode, zeroNode, box, maxC, maxH, maxW):

    visited = deque([])
    count = 0
    willVisit = [oneNode.popleft()]

    while willVisit:

        oneNode = deque(willVisit)
        willVisit = []

        while oneNode:

            c, h, w = oneNode.popleft()

            if (c, h, w) not in visited:
                visited.append((c, h, w))
                if c + 1 < maxC and box[c + 1][h][w] == '0':
                    box[c + 1][h][w] = '1'
                    willVisit.append((c + 1, h, w))
                if c - 1 > - 1 and box[c - 1][h][w] == '0':
                    box[c - 1][h][w] = '1'
                    willVisit.append((c - 1, h, w))
                if h + 1 < maxH and box[c][h + 1][w] == '0':
                    box[c][h + 1][w] = '1'
                    willVisit.append((c, h + 1, w))
                if h - 1 > - 1 and box[c][h - 1][w] == '0':
                    box[c][h - 1][w] = '1'
                    willVisit.append((c, h - 1, w))
                if w + 1 < maxW and box[c][h][w + 1] == '0':
                    box[c][h][w + 1] = '1'
                    willVisit.append((c, h, w + 1))
                if w - 1 > - 1 and box[c][h][w - 1] == '0':
                    box[c][h][w - 1] = '1'
                    willVisit.append((c, h, w - 1))

        count += 1

    return count - 1, visited

if __name__ == '__main__':

    box = []
    oneNode = deque([])
    zeroNode = deque([])

    w, h, c = map(int, stdin.readline().split())

    for i in range(c):
        box.append([])
        for j in range(h):
            box[i].append(stdin.readline().split())

    for i in range(c):
        for j in range(h):
            for k in range(w):
                if box[i][j][k] == '0':
                    zeroNode.append((i, j, k))
                elif box[i][j][k] == '1':
                    oneNode.append((i, j, k))

    if not zeroNode:
        print(0)
    else:
        result, visited = solve(oneNode, zeroNode, box, c, h, w)

        if set(zeroNode) - set(visited):
            print(-1)
        else:
            print(result)

    
    

    
