# https://www.acmicpc.net/problem/2960

N, K = map(int, input().split())
arr = [i for i in range(2, N + 1)]
visited = [1 for _ in range(N + 3)]
cnt = 0

for i in range(2, N + 1):
    for j in range(i, arr[-1] + 1, i):
        if visited[j]:
            visited[j] = 0
            cnt += 1
        if cnt == K:
            print(j)
            exit()
