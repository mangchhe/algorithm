import sys
from collections import Counter

# sys.stdin = open('input.txt', 'rt')

def comparison(a, b):
    if a < b:
        return b
    else:
        return a

n = int(input())

result = 0

for i in range(n):
    a  = Counter(map(int, input().split()))
    val, pre = sorted(a.items(), key=lambda x: (-x[1], -x[0]))[0]
    if pre == 3:
        result = comparison(result, 10000 + val * 1000)
    elif pre == 2:
        result = comparison(result, 1000 + val * 100)
    else:
        result = comparison(result, 100 * val)

print(result)
