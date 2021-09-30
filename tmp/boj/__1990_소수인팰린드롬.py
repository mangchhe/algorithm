# https://www.acmicpc.net/problem/1990

# 10000000 이상은 팰린드롬이면서 소수인 수가 없다.

import math
input = __import__('sys').stdin.readline

a, b = map(int, input().split())

for i in map(str, range(a, min(b + 1, 10000000))):
    if i == i[::-1]:
        n = int(i)
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                break
        else:
            print(n)

print(-1)
