# https://www.acmicpc.net/problem/1715

from heapq import heappush, heappop

input = __import__('sys').stdin.readline

h = []
ans = 0

for _ in range(int(input())):
    heappush(h, int(input()))

while len(h) != 1:
    a = heappop(h)
    b = heappop(h)
    c = a + b
    heappush(h, c)
    ans += c

print(ans)
