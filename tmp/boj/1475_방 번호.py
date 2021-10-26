# https://www.acmicpc.net/problem/1475

from collections import defaultdict

dozen = defaultdict(int)
ans = 0

for n in list(map(int, list(input()))):
    if n == 6 or n == 9:
        dozen[6] += 1
        ans = max(ans, int(dozen[6] / 2 + .5))
    else:
        dozen[n] += 1
        ans = max(ans, dozen[n])

print(ans)
