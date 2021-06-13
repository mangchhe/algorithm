from itertools import combinations
from copy import deepcopy
from functools import reduce
from collections import deque

input = __import__("sys").stdin.readline

MI = lambda: map(int, input().split())
N, M, D = MI()
map = [list(MI()) for _ in range(N)]
archers = combinations([i for i in range(M)], 3)
res = 0
dx = [0, -1, 0]
dy = [-1, 0, 1]


def bfs(x, y, map, attackList):

    q = deque([(x - 1, y)])
    visited = [[0] * M for _ in range(N)]
    visited[x - 1][y] = 1

    if map[x - 1][y] == 1:
        attackList.add((x - 1, y))
        return

    while q:
        qx, qy = q.popleft()
        for i in range(3):
            tx = qx + dx[i]
            ty = qy + dy[i]
            if -1 < tx and -1 < ty < M:
                if not visited[tx][ty] and abs(tx - x) + abs(ty - y) <= D:
                    visited[tx][ty] = 1
                    q.append((tx, ty))
                    if map[tx][ty] == 1:
                        attackList.add((tx, ty))
                        return


def attack(archer, map):

    cnt = 0

    while map:
        attackList = set()

        for k in archer:
            bfs(N, k, map, attackList)

        for x, y in attackList:
            map[x][y] = 0
            cnt += 1

        map = move(map)

    return cnt


def move(map):
    if not any(reduce(lambda x, y: x + y, map)):
        return []
    else:
        for x in range(N - 1, 0, -1):
            for y in range(M):
                map[x][y] = map[x - 1][y]
        for y in range(M):
            map[0][y] = 0
        return map


for archer in archers:
    res = max(res, attack(archer, deepcopy(map)))

print(res)
