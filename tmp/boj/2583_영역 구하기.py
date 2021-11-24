input = __import__('sys').stdin.readline

M, N, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
ans = []

def coloring(arr, x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

def bfs(arr, x, y):
    q =  [(x, y)]
    arr[x][y] = 1
    ret = 1
    while q:
        x, y = q.pop()
        for cx, cy in move(x, y):
            if -1 < cx < N and -1 < cy < M and not arr[cx][cy]:
                arr[cx][cy] = 1
                ret += 1
                q.append((cx,cy))
    return ret

def move(x, y):
    yield x, y + 1
    yield x, y - 1
    yield x - 1, y
    yield x + 1, y

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    coloring(arr, x1, y1, x2 ,y2)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            ans.append(bfs(arr, i, j))

print(len(ans))
print(*sorted(ans))
