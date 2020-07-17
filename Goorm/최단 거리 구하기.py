from collections import deque

N = int(input())

NList = []

for i in range(N):

    NList.append(list(map(int, input().split())))


def bfs():

    visited = deque([[0,0]])

    while visited:

        x, y = visited.popleft()

        if x + 1 < N and NList[x + 1][y] == 1:
            NList[x + 1][y] = NList[x][y] + 1
            visited.append((x+1, y))

        if x - 1 > -1 and NList[x - 1][y] == 1:
            NList[x - 1][y] = NList[x][y] + 1
            visited.append((x - 1, y))

        if y + 1 < N and NList[x][y + 1] == 1:
            NList[x][y + 1] = NList[x][y] + 1
            visited.append((x, y + 1))

        if y - 1 > -1 and NList[x][y - 1] == 1:
            NList[x][y - 1] = NList[x][y] + 1
            visited.append((x, y - 1))

bfs()

print(NList[N-1][N-1])