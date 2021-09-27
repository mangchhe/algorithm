# https://www.acmicpc.net/problem/15686

input = __import__('sys').stdin.readline

def traverse(n, visited):
    global ans
    if len(visited) == M:
        total = 0
        for h in house:
            minVal = float('INF')
            for v in visited:
                minVal = min(minVal, abs(h[0] - v[0]) + abs(h[1] - v[1]))
            total += minVal
        ans = min(ans, total)
    elif n >= len(chicken):
        return
    else:
        for i in range(n, len(chicken)):
            visited.append(chicken[i])
            traverse(i + 1, visited)
            visited.pop()


N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
ans = float('INF')

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append((i, j))
        elif maps[i][j] == 2:
            chicken.append((i, j))

traverse(0, [])

print(ans)
