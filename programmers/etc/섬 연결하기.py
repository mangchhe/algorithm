def getParent(parent, a):

    if parent[a] == a:
        return a

    parent[a] = getParent(parent, parent[a])

    return parent[a]


def unionParent(parent, a, b):

    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(parent, a, b):

    a = getParent(parent, a)
    b = getParent(parent, b)

    if a == b:
        return 1
    else:
        return 0


def solution(n, costs):

    answer = 0
    cnt = 0
    parent = [i for i in range(n)]
    costs = sorted(costs, key=lambda x: x[2])

    for cost in costs:
        s, e, c = cost
        if find(parent, s, e):
            continue
        else:
            answer += c
            unionParent(parent, s, e)
            cnt += 1
            if cnt == n:
                break

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
