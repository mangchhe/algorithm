"""  
    작성일 : 20/10/19
    수정일 : 20/10/21
"""

import bisect
import time

n, m = map(int, input().split())
data = list(map(int, input().split()))
min = int(1e9)
max = 0

""" 
def binarySearch(target, start, end):
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

print(time.time() - start) """

right = bisect.bisect_right(data, m)
left = bisect.bisect_left(data, m)

if right - left == 0:
    print(-1)
else:
    print(right - left)

