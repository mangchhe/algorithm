def getPrime(n):
    sieve  = [True] * n
    for i in range(2, int(n ** .5) + 1):
        if not sieve[i]:
            continue
        for j in range(i * 2, n, i):
            sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]

N = int(input())
primes = getPrime(N + 1)
dp = [0] * (N + 1)
dp[0] = 1

for prime in primes:
    for i in range(prime, N + 1):
        dp[i] = (dp[i] + dp[i - prime]) % 123456789

print(dp[N])
