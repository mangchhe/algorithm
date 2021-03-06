import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

pre = set()
si = set()

for i in range(n):
    pre.add(input())

for i in range(n - 1):
    si.add(input())

print((pre ^ si).pop())

