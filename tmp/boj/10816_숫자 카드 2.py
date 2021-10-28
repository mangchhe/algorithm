# https://www.acmicpc.net/problem/10816

from collections import defaultdict, Counter

# 방법1

input()
cards = defaultdict(int)
for i in map(int, input().split()): cards[i] += 1
input()
for i in map(int, input().split()): print(cards[i], end=" ")

# 방법2

input()
a = Counter(input().split())
input()
print(*(a[v] for v in input().split()))
