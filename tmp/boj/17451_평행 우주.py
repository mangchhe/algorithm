# https://www.acmicpc.net/problem/17451

import math

N = int(input())
space = list(map(int, input().split()))

dis = [space[-1]]

for i in range(N - 2, -1, -1):
    dis.append(math.ceil(dis[-1] / space[i]) * space[i])

print(dis)

print(dis[-1])
