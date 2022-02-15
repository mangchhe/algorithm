input = __import__("sys").stdin.readline

graph = [[float("INF")] * 52 for _ in range(52)]

N = int(input())

for _ in range(N):
    x, y = 0, 0
    a = input().split()
    if ord(a[0]) < 91:
        x = ord(a[0]) - 65
    else:
        x = ord(a[0]) - 71
    if ord(a[2]) < 91:
        y = ord(a[2]) - 65
    else:
        y = ord(a[2]) - 71

    graph[x][y] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans_x, ans_y = 0, 0
ans = []

for i in range(52):
    for j in range(52):
        if i == j:
            continue
        if graph[i][j] != float("INF"):
            if i < 26:
                ans_x = 65 + i
            else:
                ans_x = 71 + i
            if j < 26:
                ans_y = 65 + j
            else:
                ans_y = 71 + j
            ans.append(chr(ans_x) + " => " + chr(ans_y))

print(len(ans))
for i in ans:
    print(i)
