def move(x, y):
    yield x, y + 1, e
    yield x, y - 1, w
    yield x + 1, y, s
    yield x - 1, y, n

def dfs(x, y, c, predict):
    global ans

    if c == N:
        ans += predict
        return

    for cx, cy, p in move(x, y):
        if not visited[cx][cy] and p != 0.0:
            visited[cx][cy] = 1
            dfs(cx, cy, c + 1, predict * p)
            visited[cx][cy] = 0

N, e, w, s, n = map(int, input().split())
e, w, s, n = e * .01, w * .01, s * .01, n * .01
visited = [[0] * 29 for _ in range(29)]
visited[14][14] = 1
ans = 0.0

dfs(14, 14, 0, 100.0)

print(ans / 100)
