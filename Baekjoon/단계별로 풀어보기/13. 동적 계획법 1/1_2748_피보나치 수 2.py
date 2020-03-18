'''
정의 : DP란 모든경우의 수를 다 계산한다. / "계산한 부분 해결값"을 사용한다.(메모이제이션)
점화식을 찾고 그 점화식을 이용한다.
EX) F[i] = F[i-1] + f[i-2]
n이 너무 큰 경우에는 분할정복기법을 이용한다.
'''

from time import time

#일반 재귀함수를 이용한 피보나치
def fibo(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

#동적프로그래밍을 이용한 피보나치
respo = {1:1,2:1}
def dp_fibo(n):

    if n not in respo:
        respo[n] = dp_fibo(n-1) + dp_fibo(n-2)

    return respo[n]

start_time = time()
#fibo(40) # 32초
dp_fibo(1000) # 0초
print(time() - start_time)