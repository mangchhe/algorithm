import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def praise(node):
    for i in superiors[node]:
        ans[i] += ans[node]
        praise(i)

N, M = map(int, input().split())
superiors = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)
for idx, n in enumerate(list(map(int, input().split())), start=1):
    if idx == 1: continue
    superiors[n].append(idx)

for _ in range(M):
    i, w = map(int, input().split())
    ans[i] += w

praise(1)
    
print(*ans[1:])
