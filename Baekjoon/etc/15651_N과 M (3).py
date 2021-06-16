N, M = map(int, input().split())


def func(visited):
    if len(visited) == M:
        print(" ".join(map(str, visited)))
    else:
        for i in range(1, N + 1):
            visited.append(i)
            func(visited)
            visited.pop()


func([])
