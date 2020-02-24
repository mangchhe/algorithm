M = int(input())
N = int(input())

NList = []

for i in range(M, N+1):
    for j in range(2,i+1):
        if i == 1:
            break
        if i / j == 1:
            NList.append(i)
            break
        if i % j == 0:
            break

if len(NList) != 0:
    print(sum(NList))
    print(min(NList))
else:
    print('-1')