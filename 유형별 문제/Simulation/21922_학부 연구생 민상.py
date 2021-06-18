# 방법1

# from sys import stdin
# from collections import deque

# input = stdin.readline

# N, M = map(int, input().split())
# map = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# q = deque([])
# #     오, 왼, 아래, 위
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# res = 0

# for i in range(N):
#     for j in range(M):
#         if map[i][j] == 9:
#             q.append((i, j, -1))
#             visited[i][j] = 1
#             res += 1

# while q:
#     x, y, d = q.popleft()
#     if d == -1:
#         for i in range(4):
#             tx = x + dx[i]
#             ty = y + dy[i]
#             if -1 < tx < N and -1 < ty < M:
#                 if not visited[tx][ty]:
#                     res += 1
#                 if map[tx][ty] == 0:
#                     visited[tx][ty] = 1
#                     q.append((tx, ty, i))
#                 elif map[tx][ty] == 1:
#                     if x != tx:
#                         q.append((tx, ty, i))
#                     visited[tx][ty] = 1
#                 elif map[tx][ty] == 2:
#                     if y != ty:
#                         q.append((tx, ty, i))
#                     visited[tx][ty] = 1
#                 elif map[tx][ty] == 3:
#                     if i == 0:
#                         q.append((tx, ty, 3))
#                     elif i == 1:
#                         q.append((tx, ty, 2))
#                     elif i == 2:
#                         q.append((tx, ty, 1))
#                     elif i == 3:
#                         q.append((tx, ty, 0))
#                     visited[tx][ty] = 1
#                 elif map[tx][ty] == 4:
#                     if i == 0:
#                         q.append((tx, ty, 2))
#                     elif i == 1:
#                         q.append((tx, ty, 3))
#                     elif i == 2:
#                         q.append((tx, ty, 0))
#                     elif i == 3:
#                         q.append((tx, ty, 1))
#                     visited[tx][ty] = 1
#     else:
#         tx = x + dx[d]
#         ty = y + dy[d]
#         if -1 < tx < N and -1 < ty < M:
#             if not visited[tx][ty]:
#                 res += 1
#             if map[tx][ty] == 0:
#                 visited[tx][ty] = 1
#                 q.append((tx, ty, d))
#             elif map[tx][ty] == 1:
#                 if x != tx:
#                     q.append((tx, ty, d))
#                 visited[tx][ty] = 1
#             elif map[tx][ty] == 2:
#                 if y != ty:
#                     q.append((tx, ty, d))
#                 visited[tx][ty] = 1
#             elif map[tx][ty] == 3:
#                 if d == 0:
#                     q.append((tx, ty, 3))
#                 elif d == 1:
#                     q.append((tx, ty, 2))
#                 elif d == 2:
#                     q.append((tx, ty, 1))
#                 elif d == 3:
#                     q.append((tx, ty, 0))
#                 visited[tx][ty] = 1
#             elif map[tx][ty] == 4:
#                 if d == 0:
#                     q.append((tx, ty, 2))
#                 elif d == 1:
#                     q.append((tx, ty, 3))
#                 elif d == 2:
#                     q.append((tx, ty, 0))
#                 elif d == 3:
#                     q.append((tx, ty, 1))
#                 visited[tx][ty] = 1

# print(res)

# 방법2

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visisted = [[0] * M for _ in range(N)]
q = []
#     오, 왼, 위, 아래
dx = [0, 0, -1, 1, 2000]
dy = [1, -1, 0, 0, 2000]
res = 0

for i in range(N):
    for j in range(M):
        if map[i][j] == 9:
            res += 1
            visisted[i][j] = 1
            for k in range(4):
                q.append((i, j, k))

dd = {
    0: [0, 1, 2, 3],
    1: [4, 4, 2, 3],
    2: [0, 1, 4, 4],
    3: [2, 3, 0, 1],
    4: [3, 2, 1, 0],
    9: [0, 1, 2, 3],
}

while q:
    x, y, d = q.pop()
    tx, ty = x + dx[dd[map[x][y]][d]], y + dy[dd[map[x][y]][d]]
    if -1 < tx < N and -1 < ty < M:
        if map[tx][ty] == 9:
            continue
        if not visisted[tx][ty]:
            res += 1
        q.append((tx, ty, dd[map[x][y]][d]))
        visisted[tx][ty] = 1

print(res)
