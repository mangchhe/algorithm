import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

before = 0
result = 0

for val in map(int, input().split()):
    if val == 1:
        before += 1
        result += before
    else:
        before = 0

print(result)