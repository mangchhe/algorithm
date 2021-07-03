from collections import defaultdict

input = __import__("sys").stdin.readline


def dfs(graph, root):

    q = [root]
    cnt = 1

    while q:
        now = q.pop()
        for i in graph[now]:
            q.append(i)
            cnt += 1

    return cnt


cnt = 0

while True:

    isStop = False
    vertex = []
    isTree = True

    while True:
        tmp = input().rstrip().split("  ")
        if tmp[-1] == "0 0":
            vertex.extend(tmp)
            break
        elif tmp[0] == "-1 -1":
            isStop = True
            break
        else:
            vertex.extend(tmp)

    cnt += 1

    if isStop:
        break

    vertex = list(
        filter(lambda x: x, list(map(lambda x: list(map(int, x.split())), vertex)))
    )

    if not vertex[: len(vertex) - 1]:
        print("Case {} is a tree.".format(cnt))
        continue

    graph = defaultdict(list)
    root = defaultdict(int)

    for i in vertex[: len(vertex) - 1]:
        graph[i[0]].append(i[1])
        root[i[0]]
        root[i[1]] += 1

    r = -1

    for i in root.items():
        if i[1] == 0 and r != -1:
            isTree = False
            break
        elif i[1] == 0:
            r = i[0]
        elif i[1] > 1:
            isTree = False
            break

    if not isTree or r == -1:
        print("Case {} is not a tree.".format(cnt))
        continue

    if dfs(graph, r) == len(vertex):
        print("Case {} is a tree.".format(cnt))
    else:
        print("Case {} is not a tree.".format(cnt))
