input = __import__('sys').stdin.readline

N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    room[i][0] = room[i - 1][0] + room[i][0]

for i in range(1, M):
    room[0][i] = room[0][i - 1] + room[0][i]

for i in range(1, N):
    for j in range(1, M):
        room[i][j] = max(room[i - 1][j], room[i][j - 1], room[i - 1][j - 1]) + room[i][j]

print(room[N - 1][M - 1])
