"""  
    작성일 : 20/10/19
"""

n, m = map(int, input().split())
data = list(map(int, input().split()))
min = int(1e9)
max = 0

def binarySearch(target, start, end):
    print('gd')
    global min, max
    if start > end:
        return None
    mid = (start + end) // 2
    if target < data[mid]:
        binarySearch(target, start, mid - 1)
    elif target > data[mid]:
        binarySearch(target, mid + 1, end)
    else:
        if data[mid - 1] == target:
            if min > mid:
                min = mid - 1
            binarySearch(target, start, mid - 1)
        if data[mid + 1] == target:
            if max < mid:
                max = mid + 1
            binarySearch(target, mid + 1, end)

binarySearch(m, 0, n - 1)

if min - max == int(1e9):
    print(-1)
else:
    print(max - min + 1)