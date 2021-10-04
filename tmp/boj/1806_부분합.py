# https://www.acmicpc.net/problem/1806

N, M = map(int, input().split())
nList = list(map(int, input().split()))

l, r, total, cnt, ans = 0, 0, 0, 0, float('INF')

while l < len(nList) or r < len(nList):
    if total < M and r < len(nList):
        total += nList[r]
        r += 1
        cnt += 1
    else:
        if total >= M:
            ans = min(ans, cnt)
        cnt -= 1
        total -= nList[l]
        l += 1

print(ans if ans != float('INF') else 0)
