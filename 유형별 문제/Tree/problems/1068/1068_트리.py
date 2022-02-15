from collections import defaultdict

input = __import__("sys").stdin.readline


def dfs(parent, graph):

    global ans

    if not graph[parent]:
        ans += 1
        return
    else:
        for i in graph[parent]:
            dfs(i, graph)


graph = defaultdict(list)

N = int(input())
nList = list(map(int, input().rstrip().split()))
M = int(input())
ans = 0
root = 0

for i, n in enumerate(nList):
    if i != M and n != M:
        graph[n].append(i)
    if n == -1:
        root = i

if M == root:
    print(0)
else:
    dfs(root, graph)
    print(ans)
