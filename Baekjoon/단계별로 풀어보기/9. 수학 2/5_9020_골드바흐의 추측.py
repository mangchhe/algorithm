from math import sqrt

NList = [val for val in range(4, 10001)]
delList = [0, 1]

for val in NList:
    for i in range(2, int(sqrt(val)) + 1):
        if val % i == 0:
            delList.append(val)
            break
        else:
            pass

tmp = list(set(NList) - set(delList))
tmp.sort()

T = int(input())

for i in range(T):
    result = []
    N = int(input())
    i = 0
    for m in range(len(tmp)):
        if N/2 < tmp[m]:
            break
        for n in range(len(tmp)):
            if tmp[m] + tmp[n] == N:
                result.append((tmp[m], tmp[n], abs(tmp[m] - tmp[n])))
                break
            elif tmp[m] + tmp[n] > N:
                break
    count = 0
    min = 9999
    for j in range(len(result)):
        if min > result[j][2]:
            count = j
            min = result[j][2]

    print(result[count][0],result[count][1])

