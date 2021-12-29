input = __import__('sys').stdin.readline

def findParent(parent, a):
    if parent[a] == a:
        return a
    parent[a] = findParent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a == b:
        return 0

    ret = cnt[a] * cnt[b]
    
    if a > b:
        parent[a] = b
        cnt[b] += cnt[a]
    else:
        parent[b] = a
        cnt[a] += cnt[b]

    return ret

if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    v = [list(map(int, input().split())) for _ in range(M)]
    connect = []
    visited = [1] * M
    for _ in range(Q):
        n = int(input()) - 1
        connect.append(n)
        visited[n] = 0

    parent = [i for i in range(N + 1)]
    cnt = [1] * (N + 1)
    ans = 0

    for i in range(M):
        if visited[i]:
            a, b = v[i]
            union(parent, a, b)
    
    for i in range(Q - 1, -1, -1):
        a, b = v[connect[i]]
        ans += union(parent, a, b)

    print(ans)
