input = __import__('sys').stdin.readline

N = int(input())
A, B = map(int, input().split())
pointDic = {}
points = []
ans = 0

for _ in range(N):
    x, y = map(int, input().split())
    pointDic[(x, y)] = 1
    points.append((x, y))

for x, y in points:
    if pointDic.get((x + A, y)) and pointDic.get((x, y + B)) and pointDic.get((x + A, y + B)):
        ans += 1

print(ans)
