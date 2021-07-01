import sys

sys.setrecursionlimit(10 ** 6)

graph = list(map(lambda x: int(x.rstrip()), sys.stdin.readlines()))


def solve(s, e):
    if s > e:
        return
    else:
        root = graph[s]
        div = e + 1
        for i in range(s + 1, e + 1):
            if graph[i] > root:
                div = i
                break

        solve(s + 1, div - 1)
        solve(div, e)
        print(root)


solve(0, len(graph) - 1)
