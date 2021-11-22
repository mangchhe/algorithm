def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

N, M = map(int, input().split())

print(M - gcd(N, M))
