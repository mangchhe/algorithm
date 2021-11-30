from collections import deque

N = int(input())
op = list(input())
s = []
words = [0] * 26

for i in range(N):
    words[i] = input()

for o in op:
    if o in ['*', '/', '+', '-']:
        b = s.pop()
        a = s.pop()
        s.append(str(eval(a + o + b)))
    else:
        s.append(words[ord(o) - 65])

print('%.2f' % (float(s[0])))


