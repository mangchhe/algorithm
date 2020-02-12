# 손익분기점
# 최초로 총 수입이 총 비용보다 많아져 많아져 이익이 발생하는 지점

A, B, C = map(int, input().split())

count = 1
benefit = C - B # C-B가 0일 경우 나눗셈에서 문제가 생길 수도 있다.

if benefit > 0:
    print((A // benefit) + 1)
else:
    print('-1')

    ''' # 오답(시간 초과)
    while True:
        if A < benefit * count:
            print(count)
            break
        elif (A - (benefit * count)) > (A - (benefit * (count-1))):
            print('-1')
            break
        else:
            count += 1
    '''