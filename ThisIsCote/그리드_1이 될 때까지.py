"""
    작성일 : 20/09/24
"""

from sys import stdin

n, k = map(int, stdin.readline().split())
count = 0

while n != 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)