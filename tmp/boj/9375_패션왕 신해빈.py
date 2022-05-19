import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    ans = 1
    kinds = {}

    for _ in range(N):
        _, kind = input().split()
        kinds[kind] = kinds.get(kind, 0) + 1
    
    for i in kinds.values():
        ans *= (i + 1)

    print(ans - 1)
