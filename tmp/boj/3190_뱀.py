from collections import deque

input = __import__('sys').stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rotate = 0
ans = 0

def change_direction(dic):
    global rotate
    if dic == 'L':
        rotate = rotate - 1 if rotate - 1 > -1 else 3
    else:
        rotate = rotate + 1 if rotate + 1 < 4 else 0

N = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

turns = {}
for _ in range(int(input())):
    inc, dic = input().split()
    turns[int(inc)] = dic

visited = [[0] * N for _ in range(N)]
visited[0][0] = 1
q = deque([(0, 0)])

while True:
    x, y = q[-1]
    cx = x + dx[rotate]
    cy = y + dy[rotate]
    ans += 1

    if cx < 0 or cx > N - 1 or cy < 0 or cy > N - 1 or visited[cx][cy]:
        break

    visited[cx][cy] = 1

    if board[cx][cy] == 1:
        board[cx][cy] = 0
        q.append((cx, cy))
    else:
        zx, zy = q.popleft()
        visited[zx][zy] = 0
        q.append((cx, cy))

    if turns.get(ans):
        change_direction(turns[ans])

print(ans)
