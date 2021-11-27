from collections import deque

input = __import__('sys').stdin.readline

N, d, k, c = map(int, input().split())
sushis = [int(input()) for _ in range(N)]
sushis = sushis + sushis[:k]
bucket = deque([])
check = [0] * 30001
cnt = 1
check[c] = 1
ans = 0

for i in range(k):
    if not check[sushis[i]]:
        cnt += 1
    check[sushis[i]] += 1
    bucket.append(sushis[i])

ans = cnt

for i in range(k, N + k):
    num = bucket.popleft()
    check[num] -= 1
    if check[num] == 0:
        cnt -= 1
    bucket.append(sushis[i])
    if check[sushis[i]] == 0:
        cnt += 1
    check[sushis[i]] += 1
    
    ans = max(ans, cnt)

print(ans)
