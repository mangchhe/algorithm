import sys

# sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())

data = list(map(int, str(n)))

for _ in range(m):
    minVal = data[0]
    for i in range(1, len(data)):
        if minVal < data[i]:
            del data[i - 1]
            break
        else:
            minVal = data[i]
    else:
        del data[-1]

for d in data:
    print(d, end='')