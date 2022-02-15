from collections import defaultdict

input = __import__("sys").stdin.readline

vertexCnt = defaultdict(int)

for i in range(int(input()) - 1):
    s, e = map(int, input().split())
    vertexCnt[s] += 1
    vertexCnt[e] += 1

for _ in range(int(input())):
    c, n = map(int, input().split())

    if c == 1:
        if vertexCnt[n] == 1:
            print("no")
        else:
            print("yes")
    else:
        print("yes")
