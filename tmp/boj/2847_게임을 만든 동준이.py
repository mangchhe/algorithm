# https://www.acmicpc.net/problem/2847

levels = [int(input()) for _ in range(int(input()))]
ans = 0

for i in range(len(levels) - 2, -1, -1):
    if levels[i] >= levels[i + 1]:
        minus = levels[i] - levels[i + 1] + 1
        levels[i] -= minus
        ans += minus

print(ans)
