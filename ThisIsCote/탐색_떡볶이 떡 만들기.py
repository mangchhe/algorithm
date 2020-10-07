""" 
    작성일 : 20/10/07
"""

from sys import stdin

def solve(array, target, start, end):

    total = 0

    mid = (start + end) // 2

    if start > end:
        return mid

    for i in array:
        if i > mid:
            total += i - mid

    if total < target:
        return solve(array, target, start, mid - 1)
    else:
        return solve(array, target, mid + 1, end)
    



n, m = map(int, input().split())

data = list(map(int, stdin.readline().rstrip().split()))

print(solve(data, m, 0, max(data)))