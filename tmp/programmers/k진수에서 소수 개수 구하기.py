def conversion(num, k):
    ret = []
    while num > 0:
        ret.append(str(num % k))
        num //= k
    return ''.join(ret[::-1])

def isPrime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
        
    return True

def solution(n, k):
    
    conversionN = conversion(n, k)
    
    ans = 0
    for n in conversionN.split('0'):
        if n and isPrime(int(n)):
            ans += 1
    
    return ans
