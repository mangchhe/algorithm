input = __import__('sys').stdin.readline

N, M, K = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
building = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for _ in range(K):
    op, n = map(int, input().split())
    if op == 1:
        if not indegree[n]:
            building[n] += 1
            if building[n] == 1:
                for i in graph[n]:
                    indegree[i] -= 1
        else:
            print("Lier!")
            break
    else:
        if building[n] == 0:
            print("Lier!")
            break
        else:
            building[n] -= 1
            if building[n] == 0:
                for i in graph[n]:
                    indegree[i] += 1
else:
    print("King-God-Emperor")
