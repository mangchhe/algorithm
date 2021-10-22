# https://www.acmicpc.net/problem/1261

import heapq

def solve(start):
    h = [(0, start)]
    distance[start[0]][start[1]] = 0

    while h:
        dis, now = heapq.heappop(h)

        if now[0] == N - 1 and now[1] == M - 1:
            return dis

        if distance[now[0]][now[1]] < dis:
            continue

        for i in range(4):
            cx = now[0] + dx[i]
            cy = now[1] + dy[i]
            if -1 < cx < N and -1 < cy < M:
                plus = 1 if maze[cx][cy] == '1' else 0
                if distance[cx][cy] > dis + plus:
                    distance[cx][cy] = dis + plus
                    heapq.heappush(h, (distance[cx][cy], (cx, cy)))

M, N = map(int, input().split())
maze = [list(input()) for _ in range(N)]
distance = [[float('INF')] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(solve((0, 0)))
