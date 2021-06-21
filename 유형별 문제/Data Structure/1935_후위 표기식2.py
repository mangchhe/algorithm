from collections import deque

input = __import__('sys').stdin.readline

N = int(input())

op = deque(list(input().rstrip()))
tmp = []

alphaNum = {}

for i in range(65, 65 + N):
    alphaNum[chr(i)] = input().rstrip()

while op:
    o = op.popleft()
    if o in ['*', '/', '+', '-']:
        a = tmp.pop()
        b = tmp.pop()
        tmp.append(str(eval(b + o + a)))
    else:
        tmp.append(alphaNum[o])

print('%.2f' % float(tmp[0]))
