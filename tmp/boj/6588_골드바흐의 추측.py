import sys
input = sys.stdin.readline

def erathos():
    for i in range(2, int(1000001 ** .5) + 1):
        for j in range(i + i, 1000001, i):
            nums[j] = 0

def setPrimes():
    for i in range(2, 1000001):
        if nums[i]:
            primes.append(i)

nums = [1] * (1000001)
primes = []

erathos()
setPrimes()

while True:
    n = int(input())
    if not n:
        break

    i = 0
    while primes[i] < n:
        if nums[n - primes[i]]:
            print(f'{n} = {primes[i]} + {n - primes[i]}')
            break
        i += 1
    else:
        print("Goldbach's conjecture is wrong.")
