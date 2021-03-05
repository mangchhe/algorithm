import sys

# sys.stdin = open('input.txt', 'rt')

data = list(input())

res = ''
op = ['+', '-', '*', '/', ')', '(']
stack = []
prio = {'+' : 3, '-' : 3, '*' : 2, '/' : 2, '(' : 1}

for d in data:
    if d in op:
        if d == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    res += stack.pop()
        else:
            while True:
                if stack and prio[d] >= prio[stack[-1]] and stack[-1] != '(':
                    res += stack.pop()
                else:
                    stack.append(d)
                    break
    else:
        res += d

for i in range(len(stack) - 1, -1, -1):
    if stack[i] in ['*', '/']:
        res += stack[i]

for s in stack:
    if s in ['+', '-']:
        res += s

print(res)