def eratos(n):
    ret = [0] * (n + 1)
    for i in range(2, int((n ** .5) + 1)):
        if ret[i]: 
            continue
        for j in range(i * 2, n + 1, i):
            ret[j] = 1

    return [i for i in range(2, n + 1) if not ret[i]]

N = int(input())
primes = eratos(N)
length = len(primes)
ans = 0

l = r = 0
_sum = 0
while l < length and r < length:
    if primes[r] + _sum <= N:
        _sum += primes[r]
        r += 1
    else:
        _sum = 0
        l = r = l + 1

    if _sum == N:
        ans += 1

print(ans)
