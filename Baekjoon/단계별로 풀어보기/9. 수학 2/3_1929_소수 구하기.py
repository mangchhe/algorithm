# 해결방안
# 1. 에라토스테네스의 체
# 2. 제곱근까지만 나누기 ○

from math import sqrt

M, N = map(int,input().split())

NList = [val for val in range(M, N+1)]
delList = [0,1]

for val in NList:
    for i in range(2, int(sqrt(val))+1):
        if val % i == 0:
            delList.append(val)
            break
        else:
            pass

result = list(set(NList) - set(delList))
result.sort()
for val in result:
    print(val)
