import sys
input = sys.stdin.readline

N, M = map(int, input().split())
relation = [[float('INF')] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    relation[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    relation[a][b] = 1
    relation[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            relation[i][j] = min(relation[i][j], relation[i][k] + relation[k][j])

ans = [float('INF')]
for i in range(1, N + 1):
    ans.append(sum(relation[i][1:]))

print(ans.index(min(ans)))
