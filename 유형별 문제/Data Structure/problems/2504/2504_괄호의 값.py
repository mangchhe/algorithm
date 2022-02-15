input = __import__('sys').stdin.readline

s = list(input().rstrip())
stack = []
ans = ''

for i in range(len(s)):
    if s[i] in ['(', '[']:
        stack.append(s[i])
    else:
        if s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                stack.append(2)
            elif len(stack) > 1 and stack[-2] == '(':
                n = stack.pop()
                stack.pop()
                stack.append(n * 2)
            else:
                stack = [0]
                break
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                stack.append(3)
            elif len(stack) > 1 and stack[-2] == '[':
                n = stack.pop()
                stack.pop()
                stack.append(n * 3)
            else:
                stack = [0]
                break
        if len(stack) > 1:
            n = stack.pop()
            m = stack.pop()
            if str(n).isdigit() and str(m).isdigit():
                stack.append(n + m)
            else:
                stack.append(m)
                stack.append(n)
if len(stack) == 1 and str(stack[-1]).isdigit():
    print(stack.pop())
else:
    print(0)
