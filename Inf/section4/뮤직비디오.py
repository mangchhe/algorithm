import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

data = list(map(int, input().split()))

s, e = 1, sum(data)
res = 0

def solve(mid):
    tmp = 0
    cnt = 0
    for d in data:
        if tmp + d <= mid:
            tmp += d
        else:
            tmp = d
            cnt += 1
    else:
        cnt += 1

    return cnt

while s <= e:

    mid = (s + e) // 2
    
    if solve(mid) <= m:
        res = mid
        e = mid - 1
    else:
        s = mid + 1

print(res)