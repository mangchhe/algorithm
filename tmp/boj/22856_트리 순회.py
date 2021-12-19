import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def inorder(node, cnt):
    global ans
    l, r = graph[node]
    if l != -1:
        ans += 1
        inorder(l, cnt + 1)
        ans += 1
    if r != -1:
        ans += 1
        inorder(r, cnt - 1)
        if cnt > -1:
            ans += 1

N = int(input())
graph = [[] for _ in range(N + 1)]
ans = 0

for _ in range(N):
    n, l, r = map(int, input().split())
    graph[n] = [l, r]

inorder(1, 0)

if graph[1][1] != -1:
    print(ans - 1)
else:
    print(ans)
