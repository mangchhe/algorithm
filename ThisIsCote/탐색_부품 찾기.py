"""
    작성일 : 20/10/07
"""

from sys import stdin

""" 이진 탐색 """

def binary_search(array, target, start, end):

    if start > end:
        return None
    
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n = int(input())
nList = list(map(int, stdin.readline().rstrip().split()))
m = int(input())
mList = list(map(int, stdin.readline().rstrip().split()))
result = []

for i in mList:
    if binary_search(nList, i, 0, n - 1) != None:
        result.append('yes')
    else:
        result.append('no')

print(result)

""" 계수 정렬 """

n = int(input())
array = [0] * 1000001

for i in map(int, stdin.readline().rstrip().split()):
    array[i] = 1

m = int(input())
result = []

for i in map(int, stdin.readline().rstrip().split()):
    if array[int(i)] == 1:
        result.append('yes')
    else:
        result.append('no')

print(result)