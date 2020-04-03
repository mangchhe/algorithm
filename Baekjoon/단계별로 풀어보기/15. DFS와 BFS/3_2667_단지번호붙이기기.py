N = int(input())

mapList = []
visited = [[0 for i in range(N)] for j in range(N)]
count = 0
countList = []

def dfs(n, m):

    global count

    count += 1
    visited[n][m] = 1

    if m+1 < N and visited[n][m+1] != 1 and mapList[n][m+1]:
        dfs(n,m+1)
    if m-1 > -1 and visited[n][m - 1] != 1 and mapList[n][m - 1]:
        dfs(n,m-1)
    if n+1 < N and visited[n + 1][m] != 1 and mapList[n + 1][m]:
        dfs(n+1,m)
    if n-1 > -1 and visited[n - 1][m] != 1 and mapList[n - 1][m]:
        dfs(n-1,m)

for _ in range(N):

    mapList.append(list(map(int, list(input()))))

for i in range(N):
    for j in range(N):
        count = 0
        if mapList[i][j] and visited[i][j] == 0:
            dfs(i,j)
            countList.append(count)

countList.sort()
print(len(countList))
for val in countList:
    print(val)