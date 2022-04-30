import sys
from collections import deque
import copy

input = sys.stdin.readline

def bfs():
    global zeroCnt, days

    while ripe:
        length = len(ripe)
        for _ in range(length):
            z, x, y = ripe.popleft()
            for cx, cy, cz in move(x, y, z):
                if not isIn(cx, cy, cz) or visited[cz][cx][cy]:
                    continue
                
                visited[cz][cx][cy] = 1
                ripe.append((cz, cx, cy))
                zeroCnt -= 1
        
        days += 1

def move(x, y, z):
    yield x + 1, y, z
    yield x - 1, y, z
    yield x, y + 1, z
    yield x, y - 1, z
    yield x, y, z + 1
    yield x, y, z - 1

def isIn(x, y, z):
    if x < 0 or x > N - 1 or y < 0 or y > M - 1 or z < 0 or z > H - 1:
        return 0
    return 1

M, N, H = map(int, input().split())
tomato = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

ripe = deque([])
zeroCnt = 0
days = 0

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                visited[k][i][j] = 1
                ripe.append((k, i, j))
            elif tomato[k][i][j] == -1:
                visited[k][i][j] = 1
            else:
                zeroCnt += 1

bfs()

if zeroCnt == 0:
    print(days - 1)
else:
    print(-1)
