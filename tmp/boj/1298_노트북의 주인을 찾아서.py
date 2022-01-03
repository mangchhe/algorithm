input = __import__('sys').stdin.readline

def dfs(now):
    for n in p[now]:
        if visited[n]: continue
        visited[n] = 1
        if not notebook[n] or dfs(notebook[n]):
            notebook[n] = now
            return 1
    return 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    p = [[] for _ in range(N + 1)]
    notebook = [0] * (N + 1)
    visited = []
    res = 0
    for _ in range(M):
        a, b = map(int, input().split())
        p[a].append(b)

    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        if dfs(i):
           res += 1

    print(res)
