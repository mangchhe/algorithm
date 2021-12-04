input = __import__('sys').stdin.readline

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def traverse(x, y):
    q = [(x, y)]
    visited[x][y] = 1
    ret = 1

    while q:
        x, y = q.pop()
        for x, y in move(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if arr[x][y] == 1 and not visited[x][y]:
                ret += 1
                visited[x][y] = 1
                q.append((x, y))
    return ret

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ans = 0

for _ in range(k):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1


for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            ans = max(ans, traverse(i, j))

print(ans)
