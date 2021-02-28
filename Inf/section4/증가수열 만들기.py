import sys

'''
수열, 증가수열, 등차수열 다른 개념
'''

# sys.stdin = open('input.txt', 'rt')

n = int(input())

data = list(map(int, input().split()))

s, e = 0, n - 1
before = 0
res = ''

while s < e:

    tmp = []

    if before < data[s]:
        tmp.append([data[s], 'L'])
    if before < data[e]:
        tmp.append([data[e], 'R'])

    tmp.sort()

    if not tmp:
        break
    else:
        res += tmp[0][1]
        before = tmp[0][0]

        if tmp[0][1] == 'L':
            s += 1
        else:
            e -= 1
            
print(len(res))
print(res)