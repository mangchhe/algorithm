import sys

sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

s, e = 0, n
mid = n // 2

while True:
    if e < s:
        break
    
    mid = (e + s) // 2

    if data[mid] == m:
        print(mid + 1)
        break
    elif data[mid] > m:
        e = mid - 1
    else:
        s = mid + 1