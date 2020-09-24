""" 
    작성일 : 20/09/24
"""

from sys import stdin

n, m = map(int, stdin.readline().split())

data = [list(map(int, stdin.readline().split())) for i in range(n)]

print(max(map(lambda x : min(x), data)))