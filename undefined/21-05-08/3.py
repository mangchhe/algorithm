def solution(n, k, cmd):

    nameList = [i for i in range(n)]
    stack = []
    now = k
    answer = ['O' for i in range(n)]

    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            now -= int(c[1])
        elif c[0] == 'D':
            now += int(c[1])
        elif c[0] == 'C':
            stack.append([now, nameList[now]])
            del nameList[now]
            if now == n - 1:
                now -= 1
            n -= 1
        elif c[0] == 'Z':
            a, b = stack.pop()
            nameList.insert(a, b)
            if now >= a:
                now += 1
            n += 1

    while stack:
        a, b = stack.pop()
        answer[b] = 'X'

    return ''.join(answer)


print(
    solution(
        8, 2,
        ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
