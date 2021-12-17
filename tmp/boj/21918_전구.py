input = __import__('sys').stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for _ in range(M):
    op, l, r = map(int, input().split())
    if op == 1:
        arr[l] = r
    elif op == 2:
        for i in range(l, r + 1):
            arr[i] ^= 1
    elif op == 3:
        for i in range(l, r + 1):
            arr[i] = 0
    elif op == 4:
        for i in range(l, r + 1):
            arr[i] = 1

print(*arr[1:])
