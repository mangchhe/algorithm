import sys

# sys.stdin = open('input.txt', 'rt')

input()
arr1 = list(map(int, input().split()))
input()
arr2 = list(map(int, input().split()))
for i in sorted(arr1 + arr2):
    print(i, end=' ')