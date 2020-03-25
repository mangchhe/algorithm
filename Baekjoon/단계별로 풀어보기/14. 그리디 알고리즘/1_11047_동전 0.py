# 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법

chageList = []
changeCount = 0

N, change = map(int,input().split())

for _ in range(N):
    tmp = int(input())
    if tmp > change:
        N -= 1
    else:
        chageList.append(tmp)

while change != 0:

    tmp = change // chageList[N-1]
    changeCount += tmp
    change -= chageList[N-1] * tmp
    N -= 1

print(changeCount)


