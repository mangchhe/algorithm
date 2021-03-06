import sys

# sys.stdin = open('input.txt', 'rt')

res = ''

def solve(n):
    s = n // 2
    h = n % 2
    if s == 0:
        return '1' 
    else:
        return solve(s) + str(h)

n = int(input())

print(solve(n))