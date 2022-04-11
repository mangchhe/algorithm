import sys
input = sys.stdin.readline

N, H = map(int, input().split())
bottom = [0] * (H + 1)
top = [0] * (H + 1)

for i in range(N):
    h = int(input())
    if i % 2 == 0:
        bottom[h] += 1
    else:
        top[h] += 1

for i in range(H - 1, 0, -1):
    bottom[i] += bottom[i + 1]
    top[i] += top[i + 1]

minVal = float('INF')
cnt = 0

for i in range(1, H + 1):
    obstacles = bottom[i] + top[H - i + 1]
    if minVal > obstacles:
        minVal = obstacles
        cnt = 1
    elif minVal == obstacles:
        cnt += 1


print(minVal, cnt)
