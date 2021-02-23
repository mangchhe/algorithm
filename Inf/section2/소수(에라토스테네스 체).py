import sys

# sys.stdin = open('input.txt', 'rt')

def isPrimeNumber(x):
    
    n = [i for i in range(x + 1)]

    for i in range(2, x + 1):
        if n[i] == 0:
            continue
        for j in range(i + i, x + 1, i):
            n[j] = 0

    return len(list(filter(lambda x : x != 0, n))) - 1

print(isPrimeNumber(int(input())))