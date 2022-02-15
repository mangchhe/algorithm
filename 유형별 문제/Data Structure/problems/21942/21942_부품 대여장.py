from collections import defaultdict
from datetime import datetime

input = __import__("sys").stdin.readline

N, L, F = input().split()

N, F = int(N), int(F)
L = int(L[:3]) * 60 * 24 + int(L[4:6]) * 60 + int(L[7:9])

borrowList = {}
ans = defaultdict(int)

for _ in range(N):
    h = input().rstrip().split()

    time = datetime(
        2021, int(h[0][5:7]), int(h[0][8:10]), int(h[1][:2]), int(h[1][3:5])
    )

    if (h[2], h[3]) in borrowList:
        ttime = (time - borrowList[(h[2], h[3])]).total_seconds() // 60
        if ttime > L:
            ans[h[3]] += (ttime - L) * F
        del borrowList[(h[2], h[3])]
    else:
        borrowList[(h[2], h[3])] = time

if ans:
    for key, value in sorted(ans.items()):
        print(key, int(value))
else:
    print(-1)
