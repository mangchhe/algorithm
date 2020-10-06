"""
    작성일 : 20/10/06
"""

from sys import stdin

n, k = map(int, input().split())

a = list(map(int, stdin.readline().rstrip().split()))
b = list(map(int, stdin.readline().rstrip().split()))

""" 
? .reverse != sort(reverse=True)
- reverse : 단순히 리스트를 뒤집는 것
- sort(reverse=True) : 내림차순으로 정렬하는 것
"""
a.sort(reverse=True)
b.sort()

for i in range(k):

    if a[-1 - i] < b[-1 - i]:
        a[-1 - i], b[-1 - i] = b[-1 - i], a[-1 - i]
    else:
        break
    
print(sum(a))
