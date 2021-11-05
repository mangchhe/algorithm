input = __import__('sys').stdin.readline

N = int(input())
items = sorted([int(input()) for _ in range(N)], reverse = True)

cnt = 0
idx = 0
ans = 0

while idx < len(items):
    cnt += 1
    if cnt % 3 == 0:
        cnt = 0
        idx += 1
        continue

    ans += items[idx]
    idx += 1

print(ans)
