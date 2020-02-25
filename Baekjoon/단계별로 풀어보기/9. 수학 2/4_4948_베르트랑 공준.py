# 해결방안
# 1. 에라토스테네스의 체
# 2. 제곱근까지만 나누기 ○ (선 계산 후 값 추출 방식)

from math import sqrt

NList = [val for val in range(2, 123456 * 2 + 1)]
delList = [0, 1]

for val in NList:
    for i in range(2, int(sqrt(val)) + 1):
        if val % i == 0:
            delList.append(val)
            break
        else:
            pass

tmp = list(set(NList) - set(delList))

while True:

    N = int(input())
    if N == 0:
        break

    print(len(list(filter(lambda x: x > N and x < N*2+1, tmp))))
