from collections import defaultdict

input = __import__("sys").stdin.readline

N, W = map(int, input().split())

vertex = defaultdict(int)

for _ in range(N - 1):
    s, e = map(int, input().split())
    vertex[s] += 1
    vertex[e] += 1

vertexCnt = len(list(filter(lambda x: x[1] == 1, vertex.items())))

if vertex[1] == 1:
    print(W / (vertexCnt - 1))
else:
    print(W / (vertexCnt))
