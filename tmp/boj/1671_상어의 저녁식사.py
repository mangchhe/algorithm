input = __import__('sys').stdin.readline

def dfs(now):
    for n in feed[now]:
        if visited[n]: continue
        visited[n] = 1
        if f[n] == -1 or dfs(f[n]):
            f[n] = now
            return 1
    return 0

if __name__ == '__main__':
    N = int(input())
    sharks = []
    for _ in range(N):
        size, speed, intell = map(int, input().split())
        sharks.append((size, speed, intell))
    feed = [[] for _ in range(N)]
    visited = []
    f = [-1] * N
    res = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            si, sp, inte = sharks[i]
            si2, sp2, inte2 = sharks[j]
            if si == si2 and sp == sp2 and inte == inte2:
                if i > j:
                    continue
                else:
                    feed[i].append(j)
            elif si >= si2 and sp >= sp2 and inte >= inte2:
                feed[i].append(j)
    
    for i in range(N):
        visited = [0] * N
        if dfs(i): res += 1
        visited = [0] * N
        if dfs(i): res += 1
    
    print(N - res)
