from sys import stdin

N, M = map(int,stdin.readline().split())

NList = [i for i in range(1, N + 1)]

idx = M - 1

result = []

while NList:

    if len(NList) > idx:

        result.append(NList.pop(idx))
        idx += M - 1

    elif len(NList) <= idx:

        idx = idx % len(NList)
        result.append(NList.pop(idx))
        idx += M - 1

print('<', end='')
while result:
    if len(result) != 1:
        print(result.pop(0), end=', ')
    else:
        print(result.pop(0), end='')
print('>', end='')