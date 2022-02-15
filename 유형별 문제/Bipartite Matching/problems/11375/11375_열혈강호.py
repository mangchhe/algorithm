import sys

input = sys.stdin.readline

def dfs(now):
    for i in em[now]:
        if visited[i]:
            continue
        visited[i] = 1
        if not w[i] or dfs(w[i]):
            w[i] = now
            return 1

    return 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    em = [[] for _ in range(N + 1)]
    w = [0] * (M + 1)
    visited = [0] * (M + 1)
    res = 0

    for i in range(1, N + 1):
        for j in list(map(int, input().split()))[1:]:
            em[i].append(j)
    
    for i in range(1, N + 1):
        visited = [0] * (M + 1)
        if dfs(i):
            res += 1

    print(res)
