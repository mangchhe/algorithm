input = __import__("sys").stdin.readline

data = list(input().rstrip())
visited = [0] * 100


def solve(s, e):

    minChr = 124
    idx = 0

    if s >= e:
        return
    else:
        for i in range(s, e):
            if minChr > ord(data[i]):
                minChr = ord(data[i])
                idx = i

    visited[idx] = 1

    for i in range(len(data)):
        if visited[i]:
            print(data[i], end="")
    print()

    solve(idx + 1, e)
    solve(s, idx)


solve(0, len(data))
