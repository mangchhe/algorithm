input = __import__('sys').stdin.readline

def dfs(now):
    for n in e[now]:
        if visited[n]: continue
        visited[n] = 1
        if not w[n] or dfs(w[n]):
            w[n] = now
            return 1
    return 0

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    e = [[] for _ in range(N + 1)]
    w = [0] * (M + 1)
    visited = []
    res = 0
    for i in range(1, N + 1):
        e[i].extend(list(map(int, input().split()))[1:])

    for i in range(1, N + 1):
        visited = [0] * (M + 1)
        if dfs(i):
            res += 1

    for i in range(1, N + 1):
        visited = [0] * (M + 1)
        while K > 0:
            if dfs(i):
                K -= 1
                res += 1
            else:
                break
        if K == 0:
            break
    
    print(res)
