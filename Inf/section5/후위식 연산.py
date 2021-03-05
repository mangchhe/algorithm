import sys

# sys.stdin = open('input.txt', 'rt')

data = list(input())

op = ['+', '-', '*', '/']
opCal = {
    '+' : lambda x, y : x + y,
    '-' : lambda x, y : x - y,
    '*' : lambda x, y : x * y,
    '/' : lambda x, y : x / y
}

stack = []

for d in data:
    if d in op:
        e = stack.pop()
        s = stack.pop()
        stack.append(opCal[d](int(s), int(e)))
    else:
        stack.append(d)

print(stack[0])