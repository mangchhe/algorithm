N, K = map(int, input().split())

d, n = 1, 1

while K > 0:
    d *= N
    N -= 1

    n *= K
    K -= 1

print((d // n) % 10007)
