def plusBit(n):
    for i in range(1, len(n) + 1):
        bits[-i] += int(n[-i])

def minusBit(n):
    for i in range(1, len(n) + 1):
        bits[-i] -= int(n[-i])

def getDecimal():
    ret = 0
    for i in range(1, 33):
        n = 1 if bits[-i] > 0 else 0
        ret += n * (2 ** (i - 1))
    return ret

if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    bits = [0] * 32

    if N == 1:
        if arr[0] == K:
            print(1, 1)
            exit()
        print(-1)
        exit()
    
    l, r = 0, 0
    plusBit(bin(arr[0])[2:])

    while l < N and r < N:
        n = getDecimal()
        if n == K:
            print(l + 1, r + 1)
            exit()
        elif n > K:
            minusBit(bin(arr[l])[2:])
            l += 1
        else:
            r += 1
            if r < N:
                plusBit(bin(arr[r])[2:])
            else:
                if getDecimal() == K:
                    print(l + 1, r)
                    exit()
                break
    while l < N:
        minusBit(bin(arr[l])[2:])
        l += 1
        n = getDecimal()
        if n == K:
            print(l + 1, r + 1)
            exit()
    print(-1)
