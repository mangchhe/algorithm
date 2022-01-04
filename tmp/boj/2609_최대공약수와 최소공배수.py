def factorization(n):
    factors = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                factors.append(i)
                break
    return factors

if __name__ == '__main__':
    a, b = map(int, input().split())
    
    aFactor = factorization(a)
    bFactor = factorization(b)

    gcd = 0
    lcm = 1

    for i in range(len(aFactor)):
        for j in range(len(bFactor)):
            if aFactor[i] == bFactor[j]:
                lcm *= aFactor[i]
                aFactor[i] = 0
                bFactor[j] = 0

    gcd = (a // lcm) * b
    
    print(lcm)
    print(gcd)
