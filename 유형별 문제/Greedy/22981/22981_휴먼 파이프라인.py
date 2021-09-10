from decimal import Decimal
from math import ceil
input = __import__('sys').stdin.readline

N, K = map(int, input().split())
v = list(map(int, input().split()))
v = sorted(v)

res = float('INF')

H = 0
H2 = 0

for i in range(N - 1):
    H += v[0]
    H2 = v[i + 1] * (N - i - 1)
    # res = min(res, K // (H + H2) + (K % (H + H2) != 0))
    res = min(res, ceil(Decimal(K) / Decimal(H + H2)))

print(res)