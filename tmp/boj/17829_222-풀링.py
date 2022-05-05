import sys
input = sys.stdin.readline

def dac(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return arr[x1][y1]

    n = (x2 - x1) // 2

    a = dac(x1, y1, x1 + n, y1 + n)
    b = dac(x1, y1 + n, x1 + n, y1 + n * 2)
    c = dac(x1 + n, y1, x1 + n * 2, y1 + n)
    d = dac(x1 + n, y1 + n, x1 + n * 2, y1 + n * 2)

    return sorted([a, b, c, d])[-2]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(dac(0, 0, N, N))
