input = __import__('sys').stdin.readline

def init():
    for i in range(N):
        if bucket[i // S][0] > arr[i]:
            bucket[i // S] = (arr[i], i)

def update(target, value):
    s = target // S
    arr[target] = value
    minVal = float('INF')
    idx = 0
    if bucket[s][0] == value:
        bucket[s] = (value, min(target, bucket[s][1]))
    if bucket[s][0] > value:
        bucket[s] = (value, target)
        return
    for i in range(s * S, (s + 1) * S if (s + 1) * S < N else N):
        if minVal > arr[i]:
            minVal = arr[i]
            idx = i

    bucket[s] = (minVal, idx)

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    S = N // int(N ** .5)
    bucket = [[float('INF'), 0] for _ in range(int(N ** .5) + 1)]

    init()

    for _ in range(N):
        op = list(map(int, input().split()))
        if op[0] == 1:
            update(op[1] - 1, op[2])
        else:
            print(sorted(bucket)[0][1] + 1)
