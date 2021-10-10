# https://www.acmicpc.net/problem/2805

# sum() 이 for loop 보다 빠름
# https://stackoverflow.com/questions/24578896/python-built-in-sum-function-vs-for-loop-performance

N, M = map(int, input().split())
namoo = list(map(int, input().split()))
ans = 0
l, r = 0, max(namoo)

while l <= r:
    mid = (l + r) // 2
    # total = 0
    # for n in namoo:
    #     if n > mid:
    #         total += n - mid
    total = sum(n - mid for n in namoo if n > mid)
    if total >= M:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)
