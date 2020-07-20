from sys import stdin

n, m = map(int,stdin.readline().split())

nList = list(map(int, stdin.readline().split()))

mList = list(map(int, stdin.readline().split()))

for i in sorted(nList + mList):

    print(i, end=' ')