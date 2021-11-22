from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = []

def move(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for cx,cy in move(x, y):
            if -1 < cx < N and -1 < cy < N and not visited[cx][cy] and arr[cx][cy] == '1':
                visited[cx][cy] = 1
                cnt += 1
                q.append((cx, cy))
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and not visited[i][j]:
            ans.append(bfs(i, j))

print(len(ans))
for i in sorted(ans):
    print(i)
                
