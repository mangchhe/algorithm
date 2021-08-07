import bisect

input = __import__("sys").stdin.readline

MI = lambda: map(int, input().split())

N = int(input())
crane = sorted(list(MI()))
M = int(input())
box = sorted(list(MI()))
canMove = [0] * (N)
res = 0

if crane[-1] < box[-1]:
    print(-1)
    exit()

for idx, c in enumerate(crane):
    canMove[idx] = bisect.bisect_right(box, c)

for i in range(N - 1, 0, -1):
    canMove[i] -= canMove[i - 1]

idx = 0

while True:
    cnt = 1
    for i in range(N - 1, -1, -1):
        if canMove[i] > 0:
            if canMove[i] - cnt < 0:
                cnt = cnt - canMove[i] + 1
                canMove[i] = 0
            else:
                canMove[i] -= cnt
                cnt = 1
        else:
            cnt += 1
    res += 1

    if sum(canMove) == 0:
        print(res)
        break
