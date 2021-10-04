# https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
nList = list(map(int, input().split()))

l, r, total, ans = 0, 0, 0, 0

while l < len(nList) or r < len(nList):
    if total < M and r < len(nList):
        total += nList[r]
        r += 1
    else:
        total -= nList[l]
        l += 1

    if total == M:
        ans += 1

print(ans)
