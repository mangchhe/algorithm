import sys

input = sys.stdin.readline

def dfs(now):
    for n in graph[now]:
        if visited[n]: continue
        visited[n] = 1
        if not w[n] or dfs(w[n]):
            w[n] = now
            return 1
    
    return 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    w = [0] * (M + 1)
    visited = []
    res = 0

    for i in range(1, N + 1):
        graph[i].extend(list(map(int, input().split()))[1:])

    for i in range(1, N + 1):
        for _ in range(2):
            visited = [0] * (M + 1)
            if dfs(i):
                res += 1

    print(res)
