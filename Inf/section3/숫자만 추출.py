import sys

# sys.stdin = open('input.txt', 'rt')

data = input()

txt = ''

for d in data:
    if ord(d) >= 48 and ord(d) <= 57:
        txt += d

txt = int(txt)
cnt = 0

for i in range(1, txt + 1):
    if txt % i == 0:
        cnt += 1

print(txt, cnt)