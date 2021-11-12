import heapq

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra(x, y):

    global ans

    h = [(0, x, y)]
    dis[x][y] = 0

    while h:
        dist, x, y = heapq.heappop(h)

        if x == N - 1 and y == N - 1:
            ans = dist
            break

        if dis[x][y] < dist:
            continue

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if -1 < cx < N and -1 < cy < N:
                if arr[cx][cy] == '0' and dis[cx][cy] > dist + 1:
                    dis[cx][cy] = dist + 1
                    heapq.heappush(h, (dist + 1, cx, cy))
                elif arr[cx][cy] == '1' and dis[cx][cy] > dist:
                    dis[cx][cy] = dist
                    heapq.heappush(h, (dist, cx, cy))

N = int(input())
arr = [list(input()) for _ in range(N)]
dis = [[float('INF')] * N for _ in range(N)]
ans = 0

dijkstra(0, 0)

print(ans)
