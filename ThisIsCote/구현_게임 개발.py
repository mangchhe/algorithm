"""
    작성일 : 20/09/25
"""

n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())

zido = [input().split() for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

result = 0
turn_count = 0

while True:

    direction -= 1

    if direction == -1:
        direction = 3
    nx = x + dx[direction]
    ny = y + dy[direction]

    if zido[nx][ny] == '0' and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_count = 0
        continue
    else:
        turn_count += 1

    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if zido[nx][ny] == 0:
            x = nx
            y = ny
            turn_count = 0
        else:
            break

print(result)

