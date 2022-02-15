input = __import__('sys').stdin.readline

def init():
    for i in range(N):
        bucket[i // section] += arr[i]

def update(idx, value):
    bucketIdx = idx // section
    bucket[bucketIdx] -= arr[idx]
    bucket[bucketIdx] += value
    arr[idx] = value
    
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
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    bucket = [0] * (int(N ** .5) + 1)
    section = N // int(N ** .5)

    init()

    for _ in range(M + K):
        op, *elements = map(int, input().split())
        if op == 1:
            update(elements[0] - 1, elements[1])
        else:
            print(getSum(elements[0] - 1, elements[1] - 1))

