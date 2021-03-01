import sys

# sys.stdin = open('input.txt', 'rt')

data = list(input())

cnt = 0
res = 0

for i in range(len(data)):

    if data[i] == '(':
        cnt += 1
        if not data[i + 1] == ')':
            res += 1
    else:
        cnt -= 1
        if data[i - 1] == '(':
            res += cnt

print(res)