import sys

# sys.stdin = open('input.txt', 'rt')

n = int(input())

data = list(map(int, input().split()))

s, e = 0, n - 1

minVal = 0

diff = 0

res = ''

while True:

    tmpArr = []

    if minVal < data[s]:
        tmpArr.append([data[s], 'L'])
    if minVal < data[e]:
        tmpArr.append([data[e], 'R'])

    tmpArr.sort()

    if not tmpArr:
        break

    if diff == 0:
        res += tmpArr[0][1]

        if minVal == 0:
            minVal = tmpArr[0][0]
            if tmpArr[0][1] == 'L':
                s += 1
            else:
                e -= 1
        else:
            diff = tmpArr[0][0] - minVal
            minVal = tmpArr[0][0]
            if tmpArr[0][1] == 'L':
                s += 1
            else:
                e -= 1
    else:
        for d in tmpArr:
            if d[0] - minVal == diff:
                res += d[1]
                minVal = d[0]
                if d[1] == 'L':
                    s += 1
                else:
                    e -= 1
                break
        else:
            break

print(res)
