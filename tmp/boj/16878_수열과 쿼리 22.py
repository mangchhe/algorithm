input = __import__('sys').stdin.readline

def init():
    for i in range(N):
        bucket[i // section] += arr[i]

def update(target, value):
    bucket[target // section] -= arr[target]
    arr[target] = value
    bucket[target // section] += value

def getSum(s, e):
    ret = 0
    l, r = s // section, e // section
    if l == r:
        for i in range(s, e + 1):
            ret += arr[i]
        return ret

    while s // section == l:
        ret += arr[s]
        s += 1
    while e // section == r:
        ret += arr[e]
        e -= 1
    for i in range(s // section, e // section + 1):
        ret += bucket[i]

    return ret

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    findQuery = {}
    updateQuery = []
    bucket = [0] * (int(N ** .5) + 1)
    section = N // int(N ** .5)

    init()

    cnt = 0
    for _ in range(int(input())):
        op, *elements = map(int, input().split())
        if op == 1:
            updateQuery.append(elements)
        else:
            if not findQuery.get(elements[0]):
                findQuery[elements[0]] = [[elements[1], elements[2], cnt]]
            else:
                findQuery[elements[0]].append([elements[1], elements[2], cnt])
            cnt += 1

    ans = [0] * cnt

    for i in range(len(updateQuery)):
        if findQuery.get(i):
            for s, e, idx in findQuery.get(i):
                ans[idx] = getSum(s - 1, e - 1)
        
        t, v = updateQuery[i]
        update(t - 1, v)
    
    if findQuery.get(len(updateQuery)):
        for s, e, idx in findQuery.get(len(updateQuery)):
            ans[idx] = getSum(s - 1, e - 1)

    for i in range(cnt):
        print(ans[i])


