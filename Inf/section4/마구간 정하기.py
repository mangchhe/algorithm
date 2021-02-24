import sys

# sys.stdin = open('input.txt', 'rt')

n, m = list(map(int, input().split()))

data = []

for i in range(n):
    data.append(int(input()))

data.sort()

s, e = 1, data[-1]
res = 0

def solve(mid):
    s, e = data[0], 0
    cnt = 1
    
    for i in range(1, n):
        e = data[i]
        
        if e - s >= mid:
            s = data[i]
            cnt += 1
        else:
            pass
    
    return cnt

while s <= e:

    mid = (s + e) // 2
    tmp = solve(mid)
    if tmp >= m:
        res = mid
        s = mid + 1
    else:
        e = mid - 1

print(res)