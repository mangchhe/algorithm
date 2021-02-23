import sys

# sys.stdin = open('input.txt', 'rt')

data = [i + 1 for i in range(20)]

for i in range(10):
    s, e = map(int, input().split())
    s -= 1
    data = data[:s] + list(reversed(data[s:e])) + data[e:20]

for d in data:
    print(d, end=' ')