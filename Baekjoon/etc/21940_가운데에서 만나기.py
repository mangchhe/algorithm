from functools import reduce

input = __import__("sys").stdin.readline

MI = lambda: map(int, input().split())

N, M = MI()
graph = [[float("INF")] * (N + 1) for _ in range(N + 1)]
res = list()

for _ in range(M):
    a, b, c = MI()
    graph[a][b] = c

for i in range(N + 1):
    graph[i][i] = 0

K = int(input())
friends = list(MI())

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 방법 1

# minVal = 0

# for i in range(1, N + 1):
#     maxVal = 0
#     for j in friends:
#         if i != j:
#             if graph[i][j] == float("INF") or graph[j][i] == float("INF"):
#                 break
#             else:
#                 maxVal = max(maxVal, graph[i][j] + graph[j][i])
#     else:
#         res.append((maxVal, i))

# minVal = min(list(zip(*res))[0])

# print(" ".join(map(str, sorted(list(zip(*filter(lambda x: x[0] == minVal, res)))[1]))))

# 방법 2

minVal = float("INF")

for i in range(1, N + 1):
    maxVal = 0
    for j in friends:
        maxVal = max(maxVal, graph[i][j] + graph[j][i])
    if minVal > maxVal:
        minVal = maxVal
        res = [i]
    elif minVal == maxVal:
        res.append(i)

print(" ".join(map(str, sorted(res))))
