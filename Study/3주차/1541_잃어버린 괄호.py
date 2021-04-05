import sys
import re

sys.stdin = open('input.txt', 'rt')

input = sys.stdin.readline

if __name__ == '__main__':

    data = input()
    tmp = list(map(str, map(int, re.split('\+|\-', data))))
    op = []
    for d in data:
        if d in ['+', '-']:
            op.append(d)
    for i, o in enumerate(op):
        tmp.insert(1 + i * 2, o)

    data = tmp

    isClose = False

    for i in range(len(data) - 1, -1, -1):
        if not isClose and data[i] not in ['+', '-']:
            data.insert(i + 1, ')')
            isClose = True
        elif data[i] == '-':
            data.insert(i + 1, '(')
            isClose = False

    data.insert(0, '(')
    print(eval(''.join(data)))