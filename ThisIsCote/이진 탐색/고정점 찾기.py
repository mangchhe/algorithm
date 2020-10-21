"""
    작성일 : 20/10/21
"""

n = int(input())
data = list(map(int, input().split()))

def bSearch(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] < mid:
        return bSearch(mid + 1, end)
    elif data[mid] > mid:
        return bSearch(start, mid - 1)
    else:
        return mid
print(bSearch(0, n - 1))