def getFactorCnt(n, factor):
    ret = 0
    while n > 0:
        n //= factor
        ret += n
    return ret

N, M = map(int, input().split())

twoFactorCnt = getFactorCnt(N, 2) - getFactorCnt(M, 2) - getFactorCnt(N - M, 2)
fiveFactorCnt = getFactorCnt(N, 5) - getFactorCnt(M, 5) - getFactorCnt(N - M, 5)

print(min(twoFactorCnt, fiveFactorCnt))
