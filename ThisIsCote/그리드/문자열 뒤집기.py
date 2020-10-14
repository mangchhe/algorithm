"""
    작성일 : 20/10/14
"""

s = list(input())

one = 0
zero = 0

tmp = s[0]
del s[0]

for i in s:
    if i == tmp:
        pass
    else:
        if tmp == '0':
            tmp = '1'
            zero += 1
        else:
            tmp = '0'
            one += 1

if tmp == '0':
    zero += 1
else:
    one += 1

if one > zero:
    print(zero)
else:
    print(one)
