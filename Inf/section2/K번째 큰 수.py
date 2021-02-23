import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

data = list(map(int, input().split()))

result = set()

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            result.add(data[i] + data[j] + data[k])

print(sorted(result, reverse=True)[m - 1])