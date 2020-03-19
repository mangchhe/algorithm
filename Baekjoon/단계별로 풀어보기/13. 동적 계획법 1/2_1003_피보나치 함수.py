respo = {0:1,1:0}

def fibo(N):

    if N not in respo:
        respo[N] = fibo(N-1) + fibo(N-2)

    return respo[N]


for i in range(int(input())):

    N = int(input())
    fibo(N)
    if N == 0:
        print(1,0)
    elif N == 1:
        print(0,1)
    else:
        print(respo[N],respo[N]+respo[N-1])

