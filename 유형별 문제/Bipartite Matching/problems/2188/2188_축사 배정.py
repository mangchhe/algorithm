input = __import__('sys').stdin.readline

def dfs(now):
    for n in cow[now]:
        if visited[n]: continue
        visited[n] = 1

        if not barn[n] or dfs(barn[n]):
            barn[n] = now
            return 1

    return 0

if __name__ == '__main__':
    N, M = map(int, input().split())
    cow = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        cow[i].extend(list(map(int, input().split()))[1:])
    barn = [0] * (M + 1)
    visited = []
    res = 0

    for i in range(1, N + 1):
        visited = [0] * (M + 1)
        if dfs(i):
            res += 1

    print(res)
