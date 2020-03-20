# 1과 00으로 이루어진 타일이 존재한다.
# 1 : 1
# 2 : 00 11
# 3 : 001 100 111
# 4 : 0000 0011 1100 1001 1111
# 5 : 00001 10000 00111 11100 10011 11001 11111 00100
# 1 2 3 5 8 = fibonacchi 와 유사

'''respo = {1:1,2:2}

def fibo(N): # 재귀함수라 스택오버플로우가 발생하여 런타임오류

    if N not in respo:

        respo[N] = fibo(N-1) + fibo(N-2)

    return respo[N] % 15746

print(fibo(int(input())))
'''

respo = {1:1,2:2}

N = int(input())

if N == 1:
    print('1')
elif N == 2:
    print('2')
else:
    for i in range(3, N+1):
        respo[i] = (respo[i-1] + respo[i-2]) % 15746 # 스택 오버플로우가 되어 -가 되는 것을 방지
    print(respo[N])