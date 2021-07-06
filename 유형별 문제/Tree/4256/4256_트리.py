input = __import__("sys").stdin.readline


def solve(root, l, r):

    for i in range(l, r):
        if preList[root] == inList[i]:
            solve(root + 1, l, i)
            solve(root + 1 + i - l, i + 1, r)
            print(preList[root], end=" ")


for _ in range(int(input())):

    N = int(input())

    preList = list(map(int, input().split()))
    inList = list(map(int, input().split()))

    solve(0, 0, N)
    print()
