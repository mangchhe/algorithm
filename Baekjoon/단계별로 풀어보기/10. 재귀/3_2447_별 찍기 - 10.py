# 구글
# 프랙탈
# 최소 단위로 쪼갤 수 있기에 분할 정복 알고리즘을 이용
# 분할 정복 알고리즘(분할, 정복, 합치기)
# 분할만 잘하면 정복은 하기가 쉽다.

N = int(input())

NList= ['***', '* *', '***']

i = 9

while True:

    if N == 3 or i > N:

        break

    tmp = []

    for j in range(i):

        if j < i // 3:

            tmp.append(NList[j] * 3)

        elif j > i // 3 * 2 - 1:

            tmp.append(NList[j - i // 3 * 2 ] * 3)

        else:

            tmp.append(NList[j - i // 3] + ' ' * (i // 3) + NList[j - i // 3])

    NList = tmp

    i *= 3

for i in NList:

    print(i)