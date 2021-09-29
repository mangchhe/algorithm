# https://www.acmicpc.net/problem/10971

# 방법 1
# 재귀

input = __import__('sys').stdin.readline

def traverse(start, cur, total):
    global ans
    if all(visited):
        if city[cur][start] != 0:
            ans = min(ans, total + city[cur][start])
    else:
        for i in range(N):
            if city[cur][i] != 0 and not visited[i]:
                visited[i] = 1
                traverse(start, i, total + city[cur][i])
                visited[i] = 0

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
ans = float('INF')
visited = [0] * N

for i in range(N):
    visited[i] = 1
    traverse(i, i, 0)
    visited[i] = 0

print(ans)
