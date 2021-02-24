import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())
data = list(map(int, input().split()))
m = int(input())

data.sort()

for i in range(m):
    data[-1] -=1
    data[0] += 1
    data.sort()

print(data[-1] - data[0])